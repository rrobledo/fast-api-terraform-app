import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.orm.base import RelationBase
from app.models.orm.product import Product


class TransactionItem(RelationBase):
    __tablename__ = "transactions_items"

    transaction_id = sa.Column(
        UUID(as_uuid=True),
        ForeignKey("transactions.id", ondelete="CASCADE"),
        primary_key=True,
    )
    product_id = sa.Column(
        UUID(as_uuid=True), ForeignKey("products.id"), primary_key=True
    )
    product = relationship(Product)

    quantity = sa.Column(sa.Integer, nullable=False)
    amount = sa.Column(sa.Float, nullable=False)
