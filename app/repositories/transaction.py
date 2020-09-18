# type: ignore
from typing import List
from uuid import UUID

from fastapi.encoders import jsonable_encoder

from app.db.session import Session
from app.models.api.transaction import TransactionCreate, TransactionUpdate
from app.models.orm.transaction import Transaction, TransactionTypes
from app.models.orm.transaction_item import TransactionItem
from app.repositories.base import BaseRepository


class TransactionRepository(
    BaseRepository[Transaction, TransactionCreate, TransactionUpdate]
):
    def create_with_items(
        self, db: Session, transaction: TransactionCreate
    ) -> Transaction:
        # Adding transaction
        db_trx = Transaction(
            type=TransactionTypes(transaction.type),
            description=transaction.description,
            amount=transaction.amount,
            user_id=transaction.user_id,
        )
        db.add(db_trx)
        db.commit()
        db.refresh(db_trx)

        # Adding items
        for item in transaction.items:
            obj_in_data = jsonable_encoder(item)
            db_item = TransactionItem(**obj_in_data)
            db_item.transaction_id = db_trx.id
            db_item.product_id = db_item.product_id
            db.add(db_item)

        db.commit()
        db.refresh(db_trx)
        return db_trx

    def find_by_user_id(self, user_id: UUID, db: Session) -> List[Transaction]:
        return db.query(self.model).filter(Transaction.user_id == user_id).all()


transaction_repo = TransactionRepository(Transaction)
