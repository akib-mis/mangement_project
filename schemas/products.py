from pydantic import BaseModel, Json
from typing import Optional, Any, Text
import json


class ProductGet(BaseModel):
    name: str
    title: str
    size: int


class ProductsDetails(ProductGet):
    model: str
    price: int
    description: str
    specification: dict
    image_url: str


class ProductReadDetails(BaseModel):
    id: Optional[int]
    name: Optional[str]
    title: Optional[str]
    description: Optional[str]
    specification: Optional[dict]
    size: Optional[int]
    model: Optional[str]
    price: Optional[int]
    image_url: Optional[str]


class ProductRequest(BaseModel):
    id: int
