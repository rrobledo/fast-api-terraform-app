# type: ignore
from app.services.api import product_service
from app.models.api.product import ProductCreate


def test_products_shall_be_success(db):
    # Create Product
    prod = ProductCreate(description="Product 01")

    prod_resp = product_service.create(prod, db)
    product = product_service.get_by_id(prod_resp.id, db)
    assert product.description == prod.description

    # Update product description
    prod.description = "new Product Description"

    prod_upd = product_service.update(product.id, prod, db)
    assert prod_upd.description == prod.description
    product = product_service.get_by_id(prod_upd.id, db)
    assert product.description == prod.description
