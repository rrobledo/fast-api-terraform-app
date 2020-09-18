# type: ignore
from app.models.api.product import ProductCreate, ProductUpdate
from app.models.orm.product import Product
from app.repositories.base import BaseRepository


class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):
    pass


product_repo = ProductRepository(Product)
