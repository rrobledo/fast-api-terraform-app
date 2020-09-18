# type: ignore
from typing import List
from uuid import UUID

from app.models.api.product import Product as ProductDto, ProductCreate, ProductUpdate

from app.db.session import Session
from app.repositories import product_repo


class ProductService:
    def create(self, product: ProductCreate, db: Session) -> ProductDto:
        product = product_repo.create(db=db, obj_in=product)
        return ProductDto.from_orm(product)

    def update(
        self, product_id: UUID, product: ProductUpdate, db: Session
    ) -> ProductDto:
        prod_db = product_repo.find(db=db, model_id=product_id)
        product = product_repo.update(db=db, db_obj=prod_db, obj_in=product)
        return ProductDto.from_orm(product)

    def get_all(self, db: Session) -> List[ProductDto]:
        return list(map(ProductDto.from_orm, product_repo.find_multi(db=db)))

    def get_by_id(self, product_id: int, db: Session) -> ProductDto:
        product = product_repo.find(db=db, model_id=product_id)
        return ProductDto.from_orm(product)


product_service = ProductService()
