from fastapi import FastAPI
from fastapi import pydantic
# input model
class Item(pydantic.BaseModel):
    id: int
    name: str =Field(...,min_length=1,max_length=100)
#output model
class ItemOut(pydantic.BaseModel):
    # id: int
    name: str
    # Tells Pydantic to read data even if it comes from ORM models (like SQLAlchemy)
    model_config = {"from_attributes": True}

items=[
        {"id":1,"name":'item1'},
         {"id":2,"name":'item2'}
    ]

# create app
app=FastAPI()


# hello world
@app.get('/')
def helloworld():
    return {'message':'hello world'}

@app.get('/Items/')
def getitems():
    return items

@app.get('/Items/search/')
def getitembyname(name):
    print(name)
    for item in items:
        if item['name']==name:
            return item
    return {'msg':'item not found'}

@app.get('/Items/{item_id}/')
def getitembyid(item_id:int):
    for item in items:
        print(item['id'])
        if item['id']==(item_id):
            return item
    return {'msg':'item not found'}


   