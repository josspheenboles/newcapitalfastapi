from fastapi import FastAPI
from sqlmodel import Field, SQLModel
from pydantic import BaseModel


class Department(SQLModel,BaseModel, table=True):
    id :int = Field(primary_key=True)
    name:str=Field(max_length=100,min_length=1)



#app
app = FastAPI()

@app.post("/departments/",response_model=Department)
def create_department(department: Department):
    return department