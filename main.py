from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint,randrange

app = FastAPI()

# pydantic is for validation only


class Post(BaseModel):
    title: str
    content: str
    shub: Optional[int] = None  # making field optional

# the actual way to pot the data


mypost = [{
  "title": "top breacsdscnjfne", "content": "Hello kartik", "id": 1},
  {"title": "bottom breacsdscnjfne", "content": "Hello @all", "id": 2}
  ]


@app.get("/")
async def root():
    return {"mesage": "There is one message for u"}


@app.get("/post")
async def post_data():
    return {"message": mypost}


@app.get("/login")
async def login():
    return "index.js"


@app.post("/create")
async def create_post(new_post: Post):
    print(new_post)
    return {"data": new_post}


# to add the entry in the already created data


@app.post("/data")
async def entry(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000)
    mypost.append(post_dict)
    return {"data": post_dict}
    print(mypost)


def find_post(id):
    for p in mypost:
        if p['id'] == id:
            return p




@app.get("/post/{id}")
async def get_post(id):
    print(id)
    post = find_post(int(id))
    print(post)
    return {"post_details": post}
