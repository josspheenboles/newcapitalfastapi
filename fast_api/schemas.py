from pydantic import BaseModel
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str

class Department(DepartmentBase):
    id: int
    employees: List["Employee"] = []

    class Config:
        from_attributes = True

class EmployeeBase(BaseModel):
    fname: str
    lname: str
    salary: int
    dno: int
    manager_id: Optional[int] = None
