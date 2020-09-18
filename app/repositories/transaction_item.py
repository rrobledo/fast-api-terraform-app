# type: ignore
from typing import List
from uuid import UUID

from app.db.session import Session
from app.models.api.transaction_item import TransactionItemCreate, TransactionItemUpdate
from app.models.orm.transaction_item import TransactionItem
from app.repositories.base import BaseRepository


class TransactionItemRepository(
    BaseRepository[TransactionItem, TransactionItemCreate, TransactionItemUpdate]
):
    def find_by_transaction_id(
        self, transaction_id: UUID, db: Session
    ) -> List[TransactionItem]:
        return (
            db.query(self.model)
            .filter(TransactionItem.transaction_id == transaction_id)
            .all()
        )


transaction_item_repo = TransactionItemRepository(TransactionItem)
