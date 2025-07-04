from fastapi import APIRouter

app = APIRouter()

@app.get("/")
def get_hello_world():
    return "hello world"
