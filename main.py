from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"mesage": "There is one message for u"}


@app.get
def get_posts():
    return {"data": "this is your post"}


@app.get("/login")
async def login():
    return "index.js"


@app.post("/create")
async def create_post(payload: dict = Body(...)):
    print(payload)
    return {"messgase": f"tile {payload['title']}successfully created "}
