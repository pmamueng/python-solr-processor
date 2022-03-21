from fastapi import FastAPI

from app.router import message

app = FastAPI()


app.include_router(message.router)


@app.get("/")
def root():
    return {"Message": "Welcome to Python-Solr-Processor"}
