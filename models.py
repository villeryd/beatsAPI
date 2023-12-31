from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    user = "user"
    admin = "admin"

# user model


class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]


class Beat:
    title: str
    artist: str
    url: Optional[url]
