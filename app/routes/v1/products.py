from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Body

from app.db.session import Session
from app.models.api.product import Product as ProductSchema
from app.models.api.product import ProductCreate, ProductUpdate
from app.services.api import product_service  # type: ignore
from app.cross.db import get_db

router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
async def get_products(db: Session = Depends(get_db),):  # type: ignore
    """Return all products"""
    return product_service.get_all(db=db)


@router.post("/", response_model=ProductSchema)
async def create_product(
    product: ProductCreate, db: Session = Depends(get_db),  # type: ignore
):
    """
    Stores a new product post
    """
    return product_service.create(db=db, product=product)


@router.get("/{product_id}", response_model=ProductSchema)
async def get_product_by_id(
    product_id: UUID, db: Session = Depends(get_db),  # type: ignore
):
    """
    Return a product by id
    """
    return product_service.get_by_id(product_id=product_id, db=db)


@router.put("/{product_id}", response_model=ProductSchema)
async def update_product(
    product_id: UUID,
    product: ProductUpdate = Body(..., embed=True),
    db: Session = Depends(get_db),  # type: ignore
):
    """
    Update a product
    """
    return product_service.update(product_id=product_id, product=product, db=db)
