from fastapi import FastAPI
import random
from typing import Optional, List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Daniel",
        last_name="Villery",
        gender=Gender.male,
        roles=[Role.user, Role.admin],
    )
]


@app.get("/")
async def root():
    return {"example": "this is an example", "data": 0}


@app.get("/users")
async def get_users():
    return db


@app.post("/users/new")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.get("/random")
def get_random():
    rn: int = random.randint(0, 100)
    return {"number": rn, "limit": 100}


@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {"number": rn, "limit": limit}


@app.get("/beats")
def get_beats():
    name: str = "name"
    artist: str = "artist"
    url: Optional[str] = None
    return {"name": name, "artist": artist, "url": url}
