from pydantic import BaseModel, Field
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str

class Socials(BaseModel):
    type: str
    link: str

class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone:  List[str]
    address: Address
    social: List[Socials]