from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instrument_membership_type import InstrumentMembershipType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstrumentMembership")


@_attrs_define
class InstrumentMembership:
    """
    Attributes:
        type (InstrumentMembershipType):
        instrument (Union[Unset, str]):
    """

    type: InstrumentMembershipType
    instrument: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type = self.type.value

        instrument = self.instrument

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if instrument is not UNSET:
            field_dict["instrument"] = instrument

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type = InstrumentMembershipType(d.pop("type"))

        instrument = d.pop("instrument", UNSET)

        instrument_membership = cls(
            type=type,
            instrument=instrument,
        )

        instrument_membership.additional_properties = d
        return instrument_membership

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
