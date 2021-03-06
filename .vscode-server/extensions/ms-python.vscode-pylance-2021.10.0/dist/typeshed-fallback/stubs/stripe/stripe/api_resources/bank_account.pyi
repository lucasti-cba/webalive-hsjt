from typing import Any

from stripe import error as error
from stripe.api_resources.abstract import (
    DeletableAPIResource as DeletableAPIResource,
    UpdateableAPIResource as UpdateableAPIResource,
    VerifyMixin as VerifyMixin,
)
from stripe.api_resources.account import Account as Account
from stripe.api_resources.customer import Customer as Customer

class BankAccount(DeletableAPIResource, UpdateableAPIResource, VerifyMixin):
    OBJECT_NAME: str
    def instance_url(self): ...
    @classmethod
    def modify(cls, sid, **params) -> None: ...
    @classmethod
    def retrieve(
        cls, id, api_key: Any | None = ..., stripe_version: Any | None = ..., stripe_account: Any | None = ..., **params
    ) -> None: ...
