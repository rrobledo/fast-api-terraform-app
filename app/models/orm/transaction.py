import sqlalchemy as sa
import enum
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.orm.base import ModelBase
from app.models.orm.transaction_item import TransactionItem
from app.models.orm.user import User


class TransactionTypes(enum.Enum):
    payment = "PAYMENT"
    cash_out = "CASH-OUT"
    transfer = "TRANSFER"


class Transaction(ModelBase):
    __tablename__ = "transactions"

    type = sa.Column(sa.Enum(TransactionTypes), nullable=False)
    description = sa.Column(sa.String(), nullable=False)
    amount = sa.Column(sa.Float, nullable=False)

    user_id = sa.Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship(User)

    items = relationship(TransactionItem)
