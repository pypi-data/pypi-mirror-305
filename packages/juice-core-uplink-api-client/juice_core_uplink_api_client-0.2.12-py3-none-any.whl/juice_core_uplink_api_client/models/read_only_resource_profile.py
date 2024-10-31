from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReadOnlyResourceProfile")


@_attrs_define
class ReadOnlyResourceProfile:
    """
    Attributes:
        value (float):
        instrument_type (Union[Unset, str]):
        category (Union[Unset, str]):
        target (Union[Unset, str]):
        unit (Union[Unset, str]):
    """

    value: float
    instrument_type: Unset | str = UNSET
    category: Unset | str = UNSET
    target: Unset | str = UNSET
    unit: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        instrument_type = self.instrument_type

        category = self.category

        target = self.target

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if instrument_type is not UNSET:
            field_dict["instrument_type"] = instrument_type
        if category is not UNSET:
            field_dict["category"] = category
        if target is not UNSET:
            field_dict["target"] = target
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        instrument_type = d.pop("instrument_type", UNSET)

        category = d.pop("category", UNSET)

        target = d.pop("target", UNSET)

        unit = d.pop("unit", UNSET)

        read_only_resource_profile = cls(
            value=value,
            instrument_type=instrument_type,
            category=category,
            target=target,
            unit=unit,
        )

        read_only_resource_profile.additional_properties = d
        return read_only_resource_profile

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
