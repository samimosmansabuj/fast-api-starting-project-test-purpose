from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.userSchema import UserSchema

app = FastAPI()

@app.get("/")
async def index():
    return {
        "message": "Hello World"
    }


@app.post("/", tags=["Create User"])
async def create_user(user: UserSchema):
    encoded = jsonable_encoder(user)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "status": True,
            "data": jsonable_encoder(user)
        } 
    )

