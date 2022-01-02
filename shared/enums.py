import enum


class OrderStatusEnum(enum.Enum):
    created = 100
    approved = 200
    prepairing = 300
    ready_for_delivery = 400
    on_delivery = 500
    delivered = 600
