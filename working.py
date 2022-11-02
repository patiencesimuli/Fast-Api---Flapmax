from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import UUID, uuid4

app = FastAPI ()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Camilla",
        last_name="Monroe",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Mohammed",
        last_name="Hussein",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def home():
    return {"Data": "Testing"}

@app.get("/api/v1/users")
async def fetch_users():
    return db
