from pydantic import BaseModel
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

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

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    department: DepartmentBase
    manager: Optional["EmployeeBase"] = None
    subordinates: List["EmployeeBase"] = []

    class Config:
        from_attributes = True

# Update forward refs for circular dependencies
Department.model_rebuild()
Employee.model_rebuild()