# type: ignore
from app.services.api import product_service
from app.services.api import transaction_service
from app.models.api.product import ProductCreate
from app.models.api.transaction import TransactionCreate, TransactionTypesBase
from app.models.api.transaction_item import TransactionItemCreate
from app.models.orm.user import User


def test_transaction_shall_be_success(db):
    # Create User
    user = User(username="rrobledo", email="raul.osvaldo.robledo@gmail.com")
    db.add(user)

    # Create Products
    prod_01 = ProductCreate(description="Product 01")
    prod_02 = ProductCreate(description="Product 01")

    prod_01 = product_service.create(prod_01, db)
    prod_02 = product_service.create(prod_02, db)

    item_01 = TransactionItemCreate(product_id=prod_01.id, quantity=1, amount=50.00)
    item_02 = TransactionItemCreate(product_id=prod_02.id, quantity=2, amount=50.00)

    transaction = TransactionCreate(
        type=TransactionTypesBase.payment,
        description="Transaction testing",
        amount=100.00,
        user_id=user.id,
        items=[item_01, item_02],
    )
    transaction_saved = transaction_service.create(user.id, transaction, db)
    assert len(transaction_saved.items) > 0
