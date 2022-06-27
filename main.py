from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title : str
    content: str
    published : bool = True

@app.get("/posts")
def root():
    return {"data": "Somebody liked my post"}

@app.get("/")
def root():
    return {"message": "Hello World1 !!!!"}

# @app.post("/createposts")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"new_post": f"Title : {payload['title']} and Content : {payload['content']} posted successfully"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post.published)
    return {"data":"new post"}