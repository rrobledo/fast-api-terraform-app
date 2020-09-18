# type: ignore
from app.models.orm.transaction import Transaction, TransactionTypes
from app.models.orm.user import User
from app.models.orm.product import Product
from app.models.orm.transaction_item import TransactionItem


def test_transactions_crd_shall_be_success(db):
    # Create User

    user = User(username="rrobledo", email="raul.osvaldo.robledo@gmail.com")
    db.add(user)
    db.commit()
    db.refresh(user)

    # Create Transaction
    trx = Transaction(
        type=TransactionTypes.payment,
        description="Payment market products",
        amount=1000.00,
        user_id=user.id,
    )
    db.add(trx)
    db.commit()
    db.refresh(trx)
    trx_db = db.query(Transaction).filter(trx.id == trx.id).first()
    assert trx_db.type == TransactionTypes.payment

    # Create Products
    prod_01 = Product(description="Product 01")
    db.add(prod_01)
    db.commit()
    db.refresh(prod_01)

    prod_02 = Product(description="Product 02")
    db.add(prod_02)
    db.commit()
    db.refresh(prod_02)

    # Insert Items to transaction
    item_01 = TransactionItem(
        transaction_id=trx.id, product_id=prod_01.id, quantity=2, amount=50.00
    )
    item_02 = TransactionItem(
        transaction_id=trx.id, product_id=prod_02.id, quantity=1, amount=50.00
    )
    db.add(item_01)
    db.add(item_02)
    db.commit()

    trx_db = db.query(Transaction).filter(trx.id == trx.id).first()
    assert len(trx_db.items) == 2

    db.query(Transaction).filter(id == trx.id).delete()
    transactions = db.query(Transaction).filter(id == trx.id).all()
    assert len(transactions) == 0
