from fastapi import FastAPI
from pydantic import BaseModel

class Itemrequest(BaseModel):
    name: str
    description: str | None = None

class Itemresponse(BaseModel):
    name: str
    description: str | None = None
    id: int

app = FastAPI()

@app.post("/items/",status_code=201,response_model=Itemresponse)
def create_item(item: Itemrequest):
    return item.model_dump()
    