from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId

from pymongo import MongoClient

from schemas.blog import blogEntity
from routes import blog

app = FastAPI()

origins = [
    'https://personal-blog-frontend-react.herokuapp.com/'
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog)

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(request)
#     return PlainTextResponse(str(exc), status_code=400)

