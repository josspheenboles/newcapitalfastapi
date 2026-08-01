from fastapi import FastAPI,status

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
]


@app.get("/items/",status_code=status.HTTP_200_OK)
def read_items(pagenumber:int=0,page_size:int=0):
    if pagenumber == 0:
        return items
    else:
        start_index = (pagenumber - 1) * page_size
        end_index = start_index + page_size
        return items[start_index:end_index]
    return items


@app.get("/items/{item_id}",status_code=status.HTTP_200_OK)
def read_item(item_id:int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items/",status_code=status.HTTP_201_CREATED)
def create_item(item: dict):
    items.append(item)
    return item


@app.put("/items/{item_id}",status_code=status.HTTP_200_OK)
def update_item(item_id: int, updated_item: dict):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.patch("/items/{item_id}",status_code=status.HTTP_200_OK)
def partial_update_item(item_id: int, updated_fields: dict):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index].update(updated_fields)
            return items[index]
    return {"error": "Item not found"}

@app.delete("/items/{item_id}",status_code=status.HTTP_200_OK)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    return {"error": "Item not found"}

@app.get("/items/search",status_code=status.HTTP_200_OK)
def search_items(name: str):    
    for item in items:
        if item["name"] == name:
            # print(f"Item found: {item}")
            return item
    return {"error": "Item not found"}