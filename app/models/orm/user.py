import sqlalchemy as sa

from app.models.orm.base import ModelBase


class User(ModelBase):
    __tablename__ = "users"

    username = sa.Column(sa.String(), unique=True, nullable=False)
    email = sa.Column(sa.String(), unique=True, nullable=False)
