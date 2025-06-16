from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a welcome message.

    Returns:
        dict[str, str]: A dictionary containing a welcome message.
    """
    return {"message": "Welcome to FastAPI!"}


@app.post("/items/")
def create_item(item: Item) -> dict[str, float | str]:
    """Create an item with name and price.

    Args:
        item (Item): A Pydantic model containing name and price.

    Returns:
        dict[str, float | str]: A dictionary with the item's name and price.
    """
    return {"name": item.name, "price": item.price}
