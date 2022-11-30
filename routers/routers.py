from typing import Union
from fastapi import APIRouter, Depends, status, Header, Request
from fastapi.responses import JSONResponse
from crud.products import ProductDAL, get_product_dal
from schemas.products import ProductReadDetails, ProductsDetails, ProductGet, ProductRequest
from utils.token_verify import verify_token


router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
def get_all_products(product_dal: ProductDAL = Depends(get_product_dal), authorized: bool = Depends(verify_token)):
    if authorized:
        try:
            response = product_dal.get_all_products()
            return response
        except Exception as e:
            return JSONResponse(content=f"Error: {str(e)}", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return JSONResponse(content="unauthorized for this credentials", status_code=status.HTTP_403_FORBIDDEN)


@router.post("", status_code=status.HTTP_201_CREATED)
def post_products(
    product: ProductsDetails,
    product_dal: ProductDAL = Depends(get_product_dal),
    authorized: bool = Depends(verify_token),
):
    if authorized:
        try:
            response = product_dal.create_product(product=product)
            return response
        except Exception as e:
            return JSONResponse(content=f"Error: {str(e)}", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return JSONResponse(content="unauthorized for this credentials", status_code=status.HTTP_403_FORBIDDEN)


@router.post("/by_id")
def get_by_id(
    product_req: ProductRequest,
    product_dal: ProductDAL = Depends(get_product_dal),
    authorized: bool = Depends(verify_token),
):
    if authorized:
        try:
            product_id = product_req.id
            response = product_dal.get_product(product_id=product_id)
            if not response:
                return JSONResponse(content="Content not found", status_code=status.HTTP_404_NOT_FOUND)
            return response
        except Exception as e:
            return JSONResponse(content=f"Error: {str(e)}", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return JSONResponse(content="unauthorized for this credentials", status_code=status.HTTP_403_FORBIDDEN)
