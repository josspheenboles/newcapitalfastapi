from pydantic import BaseModel
from typing import Optional, List

class DepartmentBase(BaseModel):
    name: str
