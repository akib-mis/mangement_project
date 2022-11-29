from pydantic import BaseModel
from typing import Optional


class ProductGet(BaseModel):
    name: str
    title: str
    size: int


class ProductsDetails(ProductGet):
    model: str
    price: int
    description: str
    image_url: str


class ProductReadDetails(BaseModel):
    id: Optional[int]
    name: Optional[str]
    title: Optional[str]
    description: Optional[str]
    size: Optional[int]
    model: Optional[str]
    price: Optional[int]
    image_url: Optional[str]


class ProductRequest(BaseModel):
    id: int
