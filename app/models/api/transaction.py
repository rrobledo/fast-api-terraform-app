from pydantic import BaseModel
from typing import List

from uuid import UUID
from enum import Enum

from app.models.api.base import Base, Field
from app.models.api.transaction_item import TransactionItemCreate, TransactionItemBase


class TransactionTypesBase(str, Enum):
    payment = "PAYMENT"
    cash_out = "CASH-OUT"
    transfer = "TRANSFER"


class TransactionBase(Base):
    """
    Transaction ticket
    """

    type: TransactionTypesBase = Field(
        ...,
        description="Transaction type. Possible values are: PAYMENT, CASH-OUT, TRANSFER",
    )
    description: str = Field(..., description="Transaction description")
    amount: float = Field(..., description="Total transaction amount")

    user_id: UUID = Field(
        ..., description="Connected user_id that has executed the transaction"
    )

    items: List[TransactionItemBase] = Field(
        ..., description="List of transaction items"
    )


class TransactionCreate(BaseModel):
    type: TransactionTypesBase = Field(
        ...,
        description="Transaction type. Possible values are: PAYMENT, CASH-OUT, TRANSFER",
    )
    description: str = Field(..., description="Transaction description")
    amount: float = Field(..., description="Total transaction amount")

    user_id: UUID = Field(
        ..., description="Connected user_id that has executed the transaction"
    )

    items: List[TransactionItemCreate] = Field(
        ..., description="List of transaction items"
    )


class TransactionUpdate(TransactionCreate):
    pass


class TransactionInDb(TransactionBase):
    pass


class Transaction(TransactionInDb):
    pass
