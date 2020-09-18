from pydantic import BaseModel

from app.models.api.base import Base
from app.models.api.base import Field


class ProductBase(Base):
    """
    Product
    """

    description: str = Field(..., description="Product description")


class ProductCreate(BaseModel):
    description: str = Field(..., description="Product description")


class ProductUpdate(ProductCreate):
    pass


class ProductInDb(ProductBase):
    pass


class Product(ProductInDb):
    pass
