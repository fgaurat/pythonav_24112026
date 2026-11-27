from fastapi import FastAPI
from pydantic import BaseModel
from customer_dao import CustomerDAO
from  pathlib import Path
import socket
import os
app = FastAPI()

# fastapi run .\main_fastapi.py --reload 
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
    
@app.post("/items")
def create_item(item:Item):
    return {"message":"Item créé","item":item}

@app.get("/customers")
def customers():
    root_path = Path(".")
    db_file = root_path / "customers.db"
    dao = CustomerDAO(db_file)

    # # customers = dao.findAll()
    return list(dao.findAll())


@app.get("/whoami")
def whoami():
    """Indique quelle instance / quel worker a traité la requête"""
    return {"host": socket.gethostname(), "pid": os.getpid()}