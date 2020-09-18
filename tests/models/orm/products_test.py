# type: ignore
from app.models.orm.product import Product


def test_products_crud_shall_be_success(db):
    # Create Product
    prod = Product(description="Product 01")
    db.add(prod)
    db.commit()
    db.refresh(prod)
    products = db.query(Product).filter(Product.id == prod.id).all()
    assert len(products) > 0

    # Update product description
    prod.description = "new Product Description"
    db.query(Product).filter(Product.id == prod.id).update(
        {"description": prod.description}
    )
    prod_updated = db.query(Product).filter(Product.id == prod.id).first()
    assert prod.description == prod_updated.description

    # Delete Product
    db.query(Product).filter(Product.id == prod.id).delete()
    products = db.query(Product).filter(Product.id == prod.id).all()
    assert len(products) == 0
