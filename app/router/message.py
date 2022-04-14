from fastapi import APIRouter

from app import schemas
from services.rabbitmq.rabbitmq import RabbitMq

router = APIRouter(
    prefix="/message",
    tags=["Messages"]
)


@router.get("/", response_model=schemas.MessageBase)
def get_message():
    return {"id": 1, "message": "sample message"}


@router.post("/")
def send_message(message):
    rabbitmq = RabbitMq(message)
    rabbitmq.send()
    return rabbitmq.message
