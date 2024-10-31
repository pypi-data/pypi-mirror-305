from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstrumentType")


@_attrs_define
class InstrumentType:
    """
    Attributes:
        name (str):
        mnemonic (str):
        instrument_set (Union[Unset, List[str]]):
    """

    name: str
    mnemonic: str
    instrument_set: Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mnemonic = self.mnemonic

        instrument_set: Unset | list[str] = UNSET
        if not isinstance(self.instrument_set, Unset):
            instrument_set = self.instrument_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mnemonic": mnemonic,
            }
        )
        if instrument_set is not UNSET:
            field_dict["instrument_set"] = instrument_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        mnemonic = d.pop("mnemonic")

        instrument_set = cast(list[str], d.pop("instrument_set", UNSET))

        instrument_type = cls(
            name=name,
            mnemonic=mnemonic,
            instrument_set=instrument_set,
        )

        instrument_type.additional_properties = d
        return instrument_type

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
