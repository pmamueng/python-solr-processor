from fastapi import APIRouter

from app import schemas

router = APIRouter(
    prefix="/message",
    tags=["Messages"]
)


@router.get("/", response_model=schemas.MessageBase)
def get_message():
    return {"id": 1, "message": "sample message"}


@router.post("/")
def post_message(message: schemas.MessageBase):
    return message
