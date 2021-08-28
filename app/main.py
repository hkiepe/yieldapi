from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI


class Product(BaseModel):
    name: Optional[str] = None
    ean: Optional[str] = None
    gross_weight: Optional[float] = None
    parcels: Optional[list] = None
    shipment_price: Optional[list] = None
    weight_out_of_range: Optional[bool] = False


app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Hello World of FastAPI with Traefik powered by Inkontor"}


""" @app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result """


@app.put("/products/{product_id}")
async def create_product(product_id: str, product: Product):
    result = {"item_id": product_id, **product.dict()}
    if result['gross_weight'] > 40:
        result['weight_out_of_range'] = True
    return result
