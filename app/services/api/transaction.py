# type: ignore
from typing import List
from uuid import UUID

from app.models.api.transaction import Transaction as TransactionDto
from app.models.api.transaction import TransactionCreate, TransactionTypesBase
from app.models.api.transaction_item import TransactionItem as TransactionItemDto
from app.db.session import Session
from app.repositories import transaction_repo


class TransactionService:
    def create(
        self, user_id: UUID, transaction: TransactionCreate, db: Session
    ) -> TransactionDto:
        if len(transaction.items) <= 0:
            raise Exception("Transaction Items shall not be empty")

        transaction.user_id = user_id
        transaction = transaction_repo.create_with_items(db, transaction)
        items = list(map(TransactionItemDto.from_orm, transaction.items))
        transaction_dto = TransactionDto(
            id=transaction.id,
            type=TransactionTypesBase(transaction.type.value),
            created_at=transaction.created_at,
            updated_at=transaction.updated_at,
            description=transaction.description,
            amount=transaction.amount,
            user_id=transaction.user_id,
            items=items,
        )
        return transaction_dto

    def get_user_transactions(self, user_id: UUID, db: Session) -> List[TransactionDto]:
        return transaction_repo.find_by_user_id(db=db, user_id=user_id)


transaction_service = TransactionService()
