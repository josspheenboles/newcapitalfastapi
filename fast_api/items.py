from fastapi import FastAPI,status, UploadFile, File,HTTPException
from pydantic import BaseModel
from pathlib import Path
from typing import List,Annotated
import shutil
import os
from dotenv import load_dotenv


# Load variables from .env file into environment
load_dotenv()

# Directory to save uploaded files
UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(exist_ok=True)


class Item(BaseModel):
    # id: int
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str





app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
]



@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile, File(description="Upload a file")]):
    # Validate file type if necessary (e.g., allow only images)
    if file.content_type not in ["image/jpeg", "image/png", "application/pdf"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only JPEG, PNG, and PDF are allowed."
        )

    file_path = UPLOAD_DIR / file.filename
    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save the file: {str(e)}"
        )
    finally:
        await file.close()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size,
        "saved_path": str(file_path)
    }

@app.get("/items/",status_code=status.HTTP_200_OK, response_model= list[ItemResponse])
def read_items(pagenumber:int=0,page_size:int=0):
    if pagenumber == 0:
        return items
    else:
        start_index = (pagenumber - 1) * page_size
        end_index = start_index + page_size
        return items[start_index:end_index]
    return items


@app.get("/items/{item_id}",status_code=status.HTTP_200_OK,response_model=ItemResponse)
def read_item(item_id:int):
    for item in items:
        if item["id"] == item_id:
            return item
    return ItemResponse(id=0, name="Item not found")


@app.post("/items/",status_code=status.HTTP_201_CREATED,response_model=ItemResponse)
def create_item(item: Item):
    # newid=len(items) + 1
    # item_data = {"id": newid, "name": item.name}
    # items.append(item_data)
    # 'item' is automatically parsed and validated as an instance of the Item class
    item_data=item.model_dump()
    return item_data


@app.put("/items/{item_id}",status_code=status.HTTP_200_OK,response_model=ItemResponse)
def update_item(item_id: int, updated_item: Item):
    for index, itemva in enumerate(items):
        print(f"itemva: {itemva}, item_id: {item_id}")
        if itemva["id"]== item_id:
            items[index] = {"id": item_id, "name": updated_item.name}
            items[index]['name'] = updated_item.model_dump()['name']
            return items[index]
            # return ItemResponse(id=item_id, name=updated_item.name)
    return ItemResponse(id=0, name="Item not found")

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