from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

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


@app.post("/data",status_code=status.HTTP_201_CREATED)
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
async def get_post(id: int, response: Response):  # check for id type validation 
    print(id)
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not exist")
        # response.status_code = status.HTTP_404_NOT_FOUND
    return {"post_details": post}




@app.delete("/post/{id}", status_code=status.HTTP_410_GONE)
async def del_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    mypost.remove(post)
    return {"message": "deleted"}