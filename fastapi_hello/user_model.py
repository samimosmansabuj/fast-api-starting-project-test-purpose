from fastapi import FastAPI, status, Query, Path
from fastapi.responses import JSONResponse
from typing import Annotated
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: str
    is_active: bool
    password: str
    role: str | None = "Admin"
    

app = FastAPI()



users = [
    {
        "id": 1,
        "name": "Samim Osman Sabuj",
        "username": "samim",
        "email": "samim@example.com",
        "is_active": True,
        "password": "osman@123",
        "role": "Admin"
    },
    {
        "id": 2,
        "name": "Mariya Akter",
        "username": "samim",
        "email": "mariya@example.com",
        "is_active": True,
        "password": "osman@123",
        "role": "Admin"
    },
    {
        "id": 3,
        "name": "Ema Rahman",
        "username": "samim",
        "email": "ema@example.com",
        "is_active": False,
        "password": "osman@123",
        "role": "Staff"
    },
    {
        "id": 4,
        "name": "Jarifa Islam",
        "username": "samim",
        "email": "jarifa@example.com",
        "is_active": True,
        "password": "osman@123",
        "role": "Staff"
    },
    {
        "id": 5,
        "name": "Marifa Hossain",
        "username": "samim",
        "email": "marifa@example.com",
        "is_active": False,
        "password": "osman@123",
        "role": "Customer"
    },
    {
        "id": 6,
        "name": "Samim",
        "username": "samim",
        "email": "samim@gmail.com",
        "is_active": False,
        "password": "samim@123",
        "role": "Customer"
    },
    {
        "id": 7,
        "name": "Osman",
        "username": "osman",
        "email": "osman@gmail.com",
        "is_active": False,
        "password": "osman@123",
        "role": "Customer"
    },
    {
        "id": 8,
        "name": "Sabuj",
        "username": "sabuj",
        "email": "sabuj@gmail.com",
        "is_active": False,
        "password": "sabuj@123",
        "role": "Admin"
    }
]


@app.get("/", tags=["Home Page"])
async def index():
    return {
        "message": "Welcome User management!"
    }


@app.get("/users", tags=["User List"])
async def userList():
    return {
        "message": "All user list!",
        "data": users
    }


@app.get("/users/{user_id}", tags=["Get Single User"])
async def getSingleUser(user_id: Annotated[int, Path(title="User ID", ge=1)]):
    user = [user for user in users if user["id"] == user_id] or None
    return JSONResponse(
        content={
            "message": "Get Single User",
            "data": user[0]
        },
        status_code=status.HTTP_200_OK
    )


@app.put("/users/{user_id}", tags=["Update Single User"])
async def updateSingleUser(user_id: Annotated[int, Path(title="Update User", ge=1, description="Update User Details")], user: UserModel):
    print("User Model: ", user)
    user_encoding = jsonable_encoder(user)
    print("After Encoding: ", user_encoding)
    
    user_object = None
    for u in users:
        if u["id"] == user_id:
            user_object = u
            break
    
    print("Before Update: ", user_object)
    user_object.update({
        "name": user.name,
        "username": user.username,
        "email": user.email,
        "is_active": user.is_active,
        "password": user.password,
        "role": user.role,
    })
    print("After Update: ", user_object)
    
    return JSONResponse(
        content={
            "message": "Update Single User",
            "data": user_object
        },
        status_code=status.HTTP_200_OK
    )
    

