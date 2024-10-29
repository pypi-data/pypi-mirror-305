from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_flow_value_preprocessor_module_suspend_resume_form_schema import (
        OpenFlowValuePreprocessorModuleSuspendResumeFormSchema,
    )


T = TypeVar("T", bound="OpenFlowValuePreprocessorModuleSuspendResumeForm")


@_attrs_define
class OpenFlowValuePreprocessorModuleSuspendResumeForm:
    """
    Attributes:
        schema (Union[Unset, OpenFlowValuePreprocessorModuleSuspendResumeFormSchema]):
    """

    schema: Union[Unset, "OpenFlowValuePreprocessorModuleSuspendResumeFormSchema"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_flow_value_preprocessor_module_suspend_resume_form_schema import (
            OpenFlowValuePreprocessorModuleSuspendResumeFormSchema,
        )

        d = src_dict.copy()
        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, OpenFlowValuePreprocessorModuleSuspendResumeFormSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = OpenFlowValuePreprocessorModuleSuspendResumeFormSchema.from_dict(_schema)

        open_flow_value_preprocessor_module_suspend_resume_form = cls(
            schema=schema,
        )

        open_flow_value_preprocessor_module_suspend_resume_form.additional_properties = d
        return open_flow_value_preprocessor_module_suspend_resume_form

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
