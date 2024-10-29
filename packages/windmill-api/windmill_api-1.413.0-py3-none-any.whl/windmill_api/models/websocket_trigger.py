import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.websocket_trigger_extra_perms import WebsocketTriggerExtraPerms
    from ..models.websocket_trigger_filters_item import WebsocketTriggerFiltersItem


T = TypeVar("T", bound="WebsocketTrigger")


@_attrs_define
class WebsocketTrigger:
    """
    Attributes:
        path (str):
        edited_by (str):
        edited_at (datetime.datetime):
        script_path (str):
        url (str):
        is_flow (bool):
        extra_perms (WebsocketTriggerExtraPerms):
        email (str):
        workspace_id (str):
        enabled (bool):
        filters (List['WebsocketTriggerFiltersItem']):
        server_id (Union[Unset, str]):
        last_server_ping (Union[Unset, datetime.datetime]):
        error (Union[Unset, str]):
    """

    path: str
    edited_by: str
    edited_at: datetime.datetime
    script_path: str
    url: str
    is_flow: bool
    extra_perms: "WebsocketTriggerExtraPerms"
    email: str
    workspace_id: str
    enabled: bool
    filters: List["WebsocketTriggerFiltersItem"]
    server_id: Union[Unset, str] = UNSET
    last_server_ping: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        edited_by = self.edited_by
        edited_at = self.edited_at.isoformat()

        script_path = self.script_path
        url = self.url
        is_flow = self.is_flow
        extra_perms = self.extra_perms.to_dict()

        email = self.email
        workspace_id = self.workspace_id
        enabled = self.enabled
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()

            filters.append(filters_item)

        server_id = self.server_id
        last_server_ping: Union[Unset, str] = UNSET
        if not isinstance(self.last_server_ping, Unset):
            last_server_ping = self.last_server_ping.isoformat()

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "edited_by": edited_by,
                "edited_at": edited_at,
                "script_path": script_path,
                "url": url,
                "is_flow": is_flow,
                "extra_perms": extra_perms,
                "email": email,
                "workspace_id": workspace_id,
                "enabled": enabled,
                "filters": filters,
            }
        )
        if server_id is not UNSET:
            field_dict["server_id"] = server_id
        if last_server_ping is not UNSET:
            field_dict["last_server_ping"] = last_server_ping
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.websocket_trigger_extra_perms import WebsocketTriggerExtraPerms
        from ..models.websocket_trigger_filters_item import WebsocketTriggerFiltersItem

        d = src_dict.copy()
        path = d.pop("path")

        edited_by = d.pop("edited_by")

        edited_at = isoparse(d.pop("edited_at"))

        script_path = d.pop("script_path")

        url = d.pop("url")

        is_flow = d.pop("is_flow")

        extra_perms = WebsocketTriggerExtraPerms.from_dict(d.pop("extra_perms"))

        email = d.pop("email")

        workspace_id = d.pop("workspace_id")

        enabled = d.pop("enabled")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = WebsocketTriggerFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        server_id = d.pop("server_id", UNSET)

        _last_server_ping = d.pop("last_server_ping", UNSET)
        last_server_ping: Union[Unset, datetime.datetime]
        if isinstance(_last_server_ping, Unset):
            last_server_ping = UNSET
        else:
            last_server_ping = isoparse(_last_server_ping)

        error = d.pop("error", UNSET)

        websocket_trigger = cls(
            path=path,
            edited_by=edited_by,
            edited_at=edited_at,
            script_path=script_path,
            url=url,
            is_flow=is_flow,
            extra_perms=extra_perms,
            email=email,
            workspace_id=workspace_id,
            enabled=enabled,
            filters=filters,
            server_id=server_id,
            last_server_ping=last_server_ping,
            error=error,
        )

        websocket_trigger.additional_properties = d
        return websocket_trigger

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
