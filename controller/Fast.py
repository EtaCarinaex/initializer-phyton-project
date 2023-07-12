from typing import Union

from fastapi import \
    APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/fast",
                   tags=["fast"],
                   responses={404: {"description": "Not found"}})


class Item(BaseModel):
    name: str
    id: int
    isOffer: Union[bool, None] = None


@router.get("/api")
def ilk_get_metodum():
    return {"test": "Merhaba, ilk phyton kodu...."}


@router.put("/put/{item_id}")
def ilk_put_metodum(item_id: int, item: Item, q: Union[bool, None] = None):
    return {"item_name": item.name, "item_i": item.id, "request_id": item_id, "flag": q}
