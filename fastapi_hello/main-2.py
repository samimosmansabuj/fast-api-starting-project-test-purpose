from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from enum import Enum

app = FastAPI()

class Role(str, Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"
    CUSTOMER = "CUSTOMER"


users = [
    {"id": 1, "name": "Samim Osman Sabuj", "email": "samim@example.com", "age": 25, "is_active": True, "role": "Admin"},
    {"id": 2, "name": "Mariya Akter", "email": "mariya@example.com", "age": 23, "is_active": True, "role": "Admin"},
    {"id": 3, "name": "Ema Rahman", "email": "ema@example.com", "age": 24, "is_active": False, "role": "Staff"},
    {"id": 4, "name": "Jarifa Islam", "email": "jarifa@example.com", "age": 22, "is_active": True, "role": "Staff"},
    {"id": 5, "name": "Marifa Hossain", "email": "marifa@example.com", "age": 26, "is_active": False, "role": "Customer"},
]

@app.get("/")
async def home():
    return {
        "message": "Hello World!"
    }

@app.get("/users")
async def user():
    return {
        "user-list": users
    }

@app.get("/users/{user_id}")
async def user_details(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return user
    return JSONResponse(status_code=200, content={
        "status": False,
        "message": "User not found!"
    })

@app.get("/user/admin/{role}")
async def users_role_wised(role: Role):
    ROLE = role.lower()
    user = [user for user in users if user["role"].lower() == ROLE]
    if user:
        return user
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)


@app.get("/user-list")
async def user_list():
    return {
        "users": users
    }