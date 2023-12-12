from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/")
async def get_users():
    return JSONResponse(
        content=jsonable_encoder({"health": "ok!"}), status_code=status.HTTP_200_OK
    )
