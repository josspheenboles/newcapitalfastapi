from pydantic import BaseModel
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str

class Department(DepartmentBase):
    id: int
    employees: List["Employee"] = []

    class Config:
        from_attributes = True
