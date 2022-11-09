from fastapi import APIRouter
import json
from models.blog import Blog
from config.db import connection
from schemas.blog import serializeDict, serializeList
from bson import ObjectId

blog = APIRouter()

@blog.get('/blogs')
async def all_blogs():
    return serializeList(connection.personal_blog.blog.find())

@blog.get('/blog/{id}')
async def find_blog(id):
    return serializeDict(connection.personal_blog.blog.find_one({"_id":ObjectId(id)}))

@blog.post('/blog')
async def create_blog(blog: Blog):
    connection.personal_blog.blog.insert_one(dict(blog))
    return serializeList(connection.personal_blog.blog.find())

# print(dict(blog))
#     return
@blog.put('/blog/{id}')
async def update_blog(id, blog: Blog):
    connection.personal_blog.blog.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(blog)
    })
    return serializeDict(connection.personal_blog.blog.find_one({"_id":ObjectId(id)}))

@blog.delete('/blog/{id}')
async def delete_blog(id):
    return serializeDict(connection.personal_blog.blog.find_one_and_delete({"_id":ObjectId(id)}))