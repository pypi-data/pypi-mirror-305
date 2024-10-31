import asyncio
import json
from collections.abc import Iterable
from functools import cache, partial

import pandas as pd
from attrs import define
from loguru import logger as log
from merge_args import merge_args  # also makefun has a decorator that does this

from juice_core_uplink_api_client.api.rest_api import (
    get_events,
    get_fdyn_event,
    get_fdyn_event_definition,
    get_pcw,
    get_pcw_by_mnemonic,
    get_plan,
    get_plan_by_id,
    get_segment_definition_by_mnemonic,
    get_series,
    get_trajectory_engineering_segments_by_mnemonic,
    get_trajectory_event_by_mnemonic,
    get_trajectory_series_by_mnemonic,
    get_uvt_event_by_source,
    get_uvt_event_file,
)
from juice_core_uplink_api_client.client import Client

DEFAULT_START = "2020"
DEFAULT_END = "2040"
DEFAULT_TRAJECTORY = "CREMA_5_1_150lb_23_1"
DEFAULT_URL = "https://juicesoc.esac.esa.int"


def expand_column(tab: pd.DataFrame, column_name="description") -> pd.DataFrame:
    """Some tables have a description column that contains additional information.

    This function expands the description column into multiple columns.

    Parameters
    ----------
    tab (pd.DataFrame):
        table to expand, must have a description column

    Returns
    -------
    pd.DataFrame:
        a new dataframe with the description column expanded

    """
    additional_columns = []
    for d in tab[column_name]:
        if not isinstance(d, str):
            additional_columns.append({})
            continue
        values = {}
        for item in d.split(";"):
            try:
                key, value = item.split("=")
                values[key.strip()] = value.strip()
            except ValueError as e:
                # log.warning(f"Could not split item {item}")
                values[column_name] = item

        additional_columns.append(values)

    tab_ = tab.drop(columns=[column_name], inplace=False)
    newd = pd.DataFrame(additional_columns)

    return tab_.join(newd)


def convert_times(table, columns=[]):
    if isinstance(columns, str):
        columns = [columns]

    if len(columns) == 0 or columns is None:
        return table

    for col in columns:
        try:
            table[col] = pd.to_datetime(table[col]).dt.tz_localize(None)
        except Exception:
            log.warning(
                f"Could not convert column {col} to datetime. Maybe is a point event?",
            )

    return table


def table_to_timeseries(table, name=None):
    return pd.Series(data=table.value.values, index=table.epoch.values, name=name)


def pandas_convertable(
    func=None,
    time_fields=[],
    is_timeseries=False,
    expand_fields=[],
):
    if func is None:
        return partial(
            pandas_convertable,
            time_fields=time_fields,
            is_timeseries=is_timeseries,
            expand_fields=expand_fields,
        )

    from copy import copy

    @merge_args(func)
    def wrapper(*args, as_pandas=True, **kwargs):
        time_fields_ = copy(time_fields)

        series_name = None
        if is_timeseries and ("epoch" not in time_fields_):
            time_fields_ += ["epoch"]
            series_name = kwargs["series_name"] if "series_name" in kwargs else args[1]

        result = func(*args, **kwargs)  # call actual function

        # log.debug(f"Got result from API:\n{result}")

        return_first_item = False
        if not isinstance(result, Iterable) and as_pandas:
            log.debug("Result is requested as pandas but it is not iterable!")
            return_first_item = True
            result = [result]

        # convert to pandas if needed
        if as_pandas:
            log.debug("Result requested as pandas. Converting.")
            table = convert_times(
                pd.DataFrame(
                    [d.to_dict() if hasattr(d, "to_dict") else d for d in result],
                ),
                columns=time_fields_,
            )

            for f in expand_fields:
                log.debug("Expanding column %s", f)
                table = expand_column(table, column_name=f)

            if is_timeseries:
                log.debug("Is a timeseries")
                return table_to_timeseries(table, name=series_name)

            if return_first_item:
                log.debug("Returning as Series")
                return table.iloc[0]

            log.debug("Returning table")
            return table

        log.debug("Returning plain result")
        return result

    return wrapper


def synchronize_async_helper(to_await):
    async_response = []

    async def run_and_capture_result():
        r = await to_await
        async_response.append(r)

    loop = asyncio.get_event_loop()
    coroutine = run_and_capture_result()
    loop.run_until_complete(coroutine)
    return async_response[0]


@define(auto_attribs=True, eq=False)
class SHTRestInterface:
    """
    Main entry point for interacting with the Juice Core Uplink API
    """

    client: Client | None = None
    timeout: float = 40.0

    def __attrs_post_init__(self):
        if not self.client:
            self.client = Client(DEFAULT_URL)
        # self.client.timeout = self.timeout

    @cache
    @pandas_convertable
    def pcw(self):
        return get_pcw.sync(client=self.client)

    def pcw_start_end(self, pcw_mnemonic: str):
        pcw = self.pcw_by_mnemonic(pcw_mnemonic)
        events = self.events_by_source_name(pcw.sevt_file)

        end = events.query('name == "PCW3_END" ').iloc[0].time
        start = events.query('name == "PCW3_START" ').iloc[0].time
        return start, end

    @cache
    @pandas_convertable(time_fields=["start", "end"])
    def pcw_by_mnemonic(self, mnemonic: str):
        return get_pcw_by_mnemonic.sync(client=self.client, mnemonic=mnemonic)

    @cache
    @pandas_convertable(time_fields=["created"])
    def plans(self):
        """Retrieve all the plans available on the endpoint"""
        return get_plan.sync(client=self.client)

    def plan_id_by_name(self, name):
        """Retrieve the plan id from the plan name"""
        for plan in self.plans(as_pandas=False):
            if plan.name.lower().strip() == name.lower().strip():
                log.debug(f"Plan {name} has id {plan.id}")
                return plan.id

        log.warning(f"No plan with name {name} found")
        return None

    @cache
    @pandas_convertable
    def fdyn_event_definitions(self):
        return get_fdyn_event_definition.sync(client=self.client)

    @cache
    @pandas_convertable(time_fields=["start", "end"])
    def events(
        self,
        mnemonics: list[str] | str = [],
        trajectory: str = DEFAULT_TRAJECTORY,
        start: str = DEFAULT_START,
        end: str = DEFAULT_END,
    ):
        start = pd.Timestamp(start)
        end = pd.Timestamp(end)

        """Retrieve events of a given type from the endpoint"""
        if isinstance(mnemonics, str):
            mnemonics = [mnemonics]

        if len(mnemonics) == 0:
            types = self.fdyn_event_definitions()
            mnemonics = [m.mnemonic for m in types]
            log.info(f"Retrieving all known fdyn: events {mnemonics}")

        q = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "trajectory": trajectory,
            "mnemonics": mnemonics,
        }

        body = json.dumps(q)
        return get_fdyn_event.sync(client=self.client, body=body)

    @cache
    @pandas_convertable(time_fields=["start", "end"])
    def plan_segments(self, plan_id_or_name):
        """Retrieve the segments of a plan"""
        plan = self.plan(plan_id_or_name, as_pandas=False)
        return plan.segments

    @cache
    @pandas_convertable(time_fields=["start", "end"])
    def engineering_segments(
        self, trajectory: str = DEFAULT_TRAJECTORY
    ) -> pd.DataFrame:
        """Retrieve the engineering segments for a mnemonic"""
        return get_trajectory_engineering_segments_by_mnemonic.sync(
            mnemonic=trajectory,
            client=self.client,
        )

    @cache
    @pandas_convertable
    def event_files(self):
        """Get list of event files"""
        return get_uvt_event_file.sync(client=self.client)

    @cache
    @pandas_convertable(time_fields=["time"])
    def events_by_source_name(self, event_name: str):
        return get_uvt_event_by_source.sync(event_name, client=self.client)

    @cache
    @pandas_convertable
    def plan(self, plan_id_or_name):
        """Retrieve the plan from the plan id or name"""
        if isinstance(plan_id_or_name, str):
            plan_id_or_name = self.plan_id_by_name(plan_id_or_name)

        return get_plan_by_id.sync(plan_id_or_name, client=self.client)

    @cache
    @pandas_convertable
    def known_series(self, trajectory=DEFAULT_TRAJECTORY):
        """Retrieve all the series available on the endpoint"""
        return get_trajectory_series_by_mnemonic.sync(
            client=self.client,
            mnemonic=trajectory,
        )

    @cache
    @pandas_convertable(is_timeseries=True)
    def series(
        self,
        series_name,
        trajectory=DEFAULT_TRAJECTORY,
        start=DEFAULT_START,
        end=DEFAULT_END,
    ):
        """Retrieve a serie from the endpoint"""

        start = pd.Timestamp(start)
        end = pd.Timestamp(end)
        q = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "trajectory": trajectory,
            "series": series_name,
        }

        body = json.dumps(q)
        return get_series.sync(client=self.client, body=body)

    def series_multi_(
        self,
        series_names,
        trajectory=DEFAULT_TRAJECTORY,
        start=DEFAULT_START,
        end=DEFAULT_END,
    ):
        loop = asyncio.get_event_loop()
        coroutine = self.series_multi(
            series_names,
            trajectory=trajectory,
            start=start,
            end=end,
        )
        return loop.run_until_complete(coroutine)

    def series_multi(
        self,
        series_names,
        trajectory=DEFAULT_TRAJECTORY,
        start=DEFAULT_START,
        end=DEFAULT_END,
    ):
        """Retrieve multiple series from the endpoint"""

        start = pd.Timestamp(start)
        end = pd.Timestamp(end)

        out = []
        for series_name in series_names:
            q = {
                "start": start.isoformat(),
                "end": end.isoformat(),
                "trajectory": trajectory,
                "series": series_name,
            }

            body = json.dumps(q)
            got = get_series.asyncio(client=self.client, body=body)
            out.append(got)

        return asyncio.gather(*out)

    @cache
    @pandas_convertable
    def event_types(self, trajectory=DEFAULT_TRAJECTORY):
        """Retrieve all the events applicable for a trajectory"""
        return get_trajectory_event_by_mnemonic.sync(
            client=self.client,
            mnemonic=trajectory,
        )

    @cache
    def segment_definition(self, mnemonic):
        return get_segment_definition_by_mnemonic.sync(
            client=self.client,
            mnemonic=mnemonic,
        )

    @pandas_convertable
    def segment_definitions(self, mnemonics: list[str]):
        return [self.segment_definition(m) for m in mnemonics]

    @cache
    @pandas_convertable(time_fields=["start", "end"])
    def events(
        self,
        mnemonics: tuple[str] | str = [],
        trajectory: str = DEFAULT_TRAJECTORY,
        start=DEFAULT_START,
        end=DEFAULT_END,
    ):
        """Retrieve events of a given type from the endpoint"""
        if isinstance(mnemonics, str):
            mnemonics = [mnemonics]

        if len(mnemonics) == 0:
            types = self.event_types(trajectory=trajectory, as_pandas=False)
            mnemonics = [m.mnemonic for m in types]
            log.info(f"Retrieving all known events {mnemonics}")

        start = pd.Timestamp(start)
        end = pd.Timestamp(end)

        q = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "trajectory": trajectory,
            "mnemonics": mnemonics,
        }

        body = json.dumps(q)
        return get_events.sync(client=self.client, body=body)
