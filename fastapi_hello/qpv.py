from fastapi import FastAPI, status, Query, Path
from fastapi.responses import JSONResponse
from typing import Annotated

app = FastAPI()

users = [
    {"id": 1, "name": "Samim Osman Sabuj", "email": "samim@example.com", "age": 25, "is_active": True, "role": "Admin"},
    {"id": 2, "name": "Mariya Akter", "email": "mariya@example.com", "age": 23, "is_active": True, "role": "Admin"},
    {"id": 3, "name": "Ema Rahman", "email": "ema@example.com", "age": 24, "is_active": False, "role": "Staff"},
    {"id": 4, "name": "Jarifa Islam", "email": "jarifa@example.com", "age": 22, "is_active": True, "role": "Staff"},
    {"id": 5, "name": "Marifa Hossain", "email": "marifa@example.com", "age": 26, "is_active": False, "role": "Customer"},
]

fake_data: dict[str, list[dict[str, str]]] = {
    "items": [
        {"item1": "Apple"},
        {"item2": "Banana"},
        {"item3": "Mango"},
        {"item4": "Pinepple"},
    ]
}

@app.get("/all-items", tags=["All Items"])
async def all_items():
    return {
        "message": "All list!"
    }

@app.get("/all-items/{item_id}", tags=["Get Single Item"])
async def get_single_item(item_id: int):
    return {
        "message": "Get Single ID",
        "Items ID": f"{item_id}"
    }


@app.get("/user/{id}", tags=["Get Single User"])
async def getSingleUser(id: Annotated[int, Path(title="User ID")]):
    result = {
        "message": "Get User",
        "User ID": f"{id}"
    }
    if id:
        result.update({"User ID": id})
    
    return JSONResponse(
        content=result, status_code=status.HTTP_200_OK
    )


@app.put("/user/{id}", tags=["Update Single User"])
async def updateSingleUser(id: Annotated[int, Path(title="User ID")], query: Annotated[str | None, Query(title="URL Get Query")] = None):
    return {
        "message": "Update User!",
        "data": {
            "userID": id,
            "query_params": query
        }
    }


@app.get("/posts/{post_id}", tags=["Get Single Post"])
async def get_post(post_id: Annotated[int, Path(title="Single Post", ge=10, le=20)], query: str | None = None):
    result = {
        "message": "Get Post"
    }
    if post_id:
        result.update({"Post ID": post_id})
    if query:
        result.update({"Query": query})
    
    return JSONResponse(
        content=result,
        status_code=status.HTTP_200_OK
    )

@app.get("/items", tags=["Items"])
async def get_items(query: Annotated[str | None, Query(title="Get All Item", description="Item Get Description", deprecated=False, alias="Enter you query...")] = None):
# async def get_items(query: Annotated[list[str] | None, Query(max_length=10, min_length=3, pattern="^apple$")] = None):
    if query:
        fake_data.update({"query": query})
    return fake_data

@app.get("/", tags=["Home Page"])
async def index():
    # return {
    #     "status": True,
    #     "message": "This is home pages using return!"
    # }
    return JSONResponse(
        content={
            "status": True,
            "message": "This is home pages!"
        },
        status_code=status.HTTP_200_OK
    )




