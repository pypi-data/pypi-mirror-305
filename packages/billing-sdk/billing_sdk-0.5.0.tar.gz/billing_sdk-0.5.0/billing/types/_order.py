import uuid
from typing import List, TypedDict

from typing_extensions import NotRequired

from billing.types._billing_entity import BillingEntity
from billing.types._customer import Customer


class Order(BillingEntity):
    pass


class OrderWithCustomer(Order):
    customer: Customer


class OrderCreatePayload(TypedDict):
    customer_auth_service_id: uuid.UUID
    product_plan_ids: List[str]


class OrderListParams(TypedDict):
    customer_auth_service_id: NotRequired[uuid.UUID]
