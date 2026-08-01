from fastapi import FastAPI
from pydantic import BaseModel

items=[   ]

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


   