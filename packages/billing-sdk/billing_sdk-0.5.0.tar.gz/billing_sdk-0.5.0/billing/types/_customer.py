import uuid

from billing.types._billing_entity import BillingEntity


class Customer(BillingEntity):
    auth_service_id: uuid.UUID
