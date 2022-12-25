# Tags

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post(
    "/create_items/",
    response_model=Item,
    tags=["items"],
    summary="Create an item here",
    description="Create an item with all the information, name, description, price",
    response_description="The response of the returned item",
    deprecated=True
)
async def create_item(item: Item):
    return item


@app.get("/read_items/", tags=["items"])
async def read_items():
    return [
        {"name": "Foo", "price": 42}
    ]


@app.get("/read_users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items])
async def get_items():
    """
    Retrieve all items and their information:

    - **name**: each item must have a name
    - **description**: each item must have a description
    - __tax__: the tax of each item is Optional
    """
    return ["Portal gun", "Plumbus"]

