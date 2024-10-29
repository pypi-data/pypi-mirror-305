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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from cdp.client.models.balance import Balance
from typing import Optional, Set
from typing_extensions import Self

class EthereumValidatorMetadata(BaseModel):
    """
    An Ethereum validator.
    """ # noqa: E501
    index: StrictStr = Field(description="The index of the validator in the validator set.")
    public_key: StrictStr = Field(description="The public key of the validator.")
    withdrawal_address: StrictStr = Field(description="The address to which the validator's rewards are sent.")
    slashed: StrictBool = Field(description="Whether the validator has been slashed.")
    activation_epoch: StrictStr = Field(description="The epoch at which the validator was activated.", alias="activationEpoch")
    exit_epoch: StrictStr = Field(description="The epoch at which the validator exited.", alias="exitEpoch")
    withdrawable_epoch: StrictStr = Field(description="The epoch at which the validator can withdraw.", alias="withdrawableEpoch")
    balance: Balance
    effective_balance: Balance
    __properties: ClassVar[List[str]] = ["index", "public_key", "withdrawal_address", "slashed", "activationEpoch", "exitEpoch", "withdrawableEpoch", "balance", "effective_balance"]

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
        """Create an instance of EthereumValidatorMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict['balance'] = self.balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_balance
        if self.effective_balance:
            _dict['effective_balance'] = self.effective_balance.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EthereumValidatorMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "public_key": obj.get("public_key"),
            "withdrawal_address": obj.get("withdrawal_address"),
            "slashed": obj.get("slashed"),
            "activationEpoch": obj.get("activationEpoch"),
            "exitEpoch": obj.get("exitEpoch"),
            "withdrawableEpoch": obj.get("withdrawableEpoch"),
            "balance": Balance.from_dict(obj["balance"]) if obj.get("balance") is not None else None,
            "effective_balance": Balance.from_dict(obj["effective_balance"]) if obj.get("effective_balance") is not None else None
        })
        return _obj


