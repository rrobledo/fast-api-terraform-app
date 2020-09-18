from typing import List

from fastapi import APIRouter, Depends

from app.db.session import Session
from app.models.api.transaction import (
    Transaction as TransactionSchema,
    TransactionCreate,
)
from app.cross.db import get_db
from app.cross import security as api_security
from app.services.api import transaction_service  # type: ignore


router = APIRouter()


@router.get("/", response_model=List[TransactionSchema])
async def get_transactions(
    db: Session = Depends(get_db),  # type: ignore
    user_id: str = Depends(api_security.get_auth_user_id),  # type: ignore
):
    """Return user's transactions"""
    return transaction_service.get_user_transactions(user_id=user_id, db=db)


@router.post("/", response_model=TransactionSchema)
async def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),  # type: ignore
    user_id: str = Depends(api_security.get_auth_user_id),  # type: ignore
):
    """
    Stores a new transaction
    """
    return transaction_service.create(user_id=user_id, transaction=transaction, db=db)
