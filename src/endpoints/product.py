from fastapi import APIRouter
from src.models.product import ProductModel
from typing import Optional

# APIRouter creates path operations for product model
route = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={
        404: {"description": "Not found"}
    })

@route.get("/")
async def get_root():
    return {"message": "Hello World"}

@route.get("/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id, "name": "Product 1", "description": "This is a product", "price": 100}

@route.post("/")
async def create_product(product: ProductModel):
    return {"product_id": product.product_id, "name": product.name, "description": product.description, "price": product.price}

@route.put("/{product_id}")
async def update_product(product_id: int, product: ProductModel):
    return {"product_id": product_id, "name": product.name, "description": product.description, "price": product.price}

@route.delete("/{product_id}")
async def delete_product(product_id: int):
    return {"product_id": product_id}