from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrajectoryList")


@_attrs_define
class TrajectoryList:
    """
    Attributes:
        name (str):
        mnemonic (str):
        id (Union[Unset, int]):
        trajectory_type (Union[Unset, str]):
    """

    name: str
    mnemonic: str
    id: Unset | int = UNSET
    trajectory_type: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mnemonic = self.mnemonic

        id = self.id

        trajectory_type = self.trajectory_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mnemonic": mnemonic,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if trajectory_type is not UNSET:
            field_dict["trajectory_type"] = trajectory_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        mnemonic = d.pop("mnemonic")

        id = d.pop("id", UNSET)

        trajectory_type = d.pop("trajectory_type", UNSET)

        trajectory_list = cls(
            name=name,
            mnemonic=mnemonic,
            id=id,
            trajectory_type=trajectory_type,
        )

        trajectory_list.additional_properties = d
        return trajectory_list

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
