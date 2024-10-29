# coding: utf-8

"""
    Coinbase Platform API

    This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

    The version of the OpenAPI document: 0.0.1-alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EthereumTransactionFlattenedTrace(BaseModel):
    """
    EthereumTransactionFlattenedTrace
    """ # noqa: E501
    error: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    to: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    gas: Optional[StrictInt] = None
    gas_used: Optional[StrictInt] = None
    input: Optional[StrictStr] = None
    output: Optional[StrictStr] = None
    sub_traces: Optional[StrictInt] = None
    trace_address: Optional[List[StrictInt]] = None
    trace_type: Optional[StrictStr] = None
    call_type: Optional[StrictStr] = None
    trace_id: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    block_hash: Optional[StrictStr] = None
    block_number: Optional[StrictInt] = None
    transaction_hash: Optional[StrictStr] = None
    transaction_index: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["error", "type", "from", "to", "value", "gas", "gas_used", "input", "output", "sub_traces", "trace_address", "trace_type", "call_type", "trace_id", "status", "block_hash", "block_number", "transaction_hash", "transaction_index"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EthereumTransactionFlattenedTrace from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EthereumTransactionFlattenedTrace from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "error": obj.get("error"),
            "type": obj.get("type"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "value": obj.get("value"),
            "gas": obj.get("gas"),
            "gas_used": obj.get("gas_used"),
            "input": obj.get("input"),
            "output": obj.get("output"),
            "sub_traces": obj.get("sub_traces"),
            "trace_address": obj.get("trace_address"),
            "trace_type": obj.get("trace_type"),
            "call_type": obj.get("call_type"),
            "trace_id": obj.get("trace_id"),
            "status": obj.get("status"),
            "block_hash": obj.get("block_hash"),
            "block_number": obj.get("block_number"),
            "transaction_hash": obj.get("transaction_hash"),
            "transaction_index": obj.get("transaction_index")
        })
        return _obj


