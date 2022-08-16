from fastapi import APIRouter
from src.endpoints import user, product

router = APIRouter()
router.include_router(user.route)
router.include_router(product.route)