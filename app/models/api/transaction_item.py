from pydantic import BaseModel

from uuid import UUID

from app.models.api.base import RelationBase
from app.models.api.base import Field


class TransactionItemBase(RelationBase):
    """
    TransactionItem
    """

    transaction_id: UUID = Field(..., description="Transaction Id")
    product_id: UUID = Field(..., description="Product Id")

    quantity: int = Field(..., description="Quantity of items")
    amount: float = Field(..., description="Amount")


class TransactionItemCreate(BaseModel):
    product_id: UUID = Field(..., description="Product Id")

    quantity: int = Field(..., description="Quantity of items")
    amount: float = Field(..., description="Amount")


class TransactionItemUpdate(TransactionItemCreate):
    pass


class TransactionItemInDb(TransactionItemBase):
    pass


class TransactionItem(TransactionItemInDb):
    pass
