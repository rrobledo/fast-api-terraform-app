import sqlalchemy as sa

from app.models.orm.base import ModelBase


class Product(ModelBase):
    __tablename__ = "products"

    description = sa.Column(sa.String(), nullable=False)
