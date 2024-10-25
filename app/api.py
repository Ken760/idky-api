from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from typing import Annotated


users = []

app = FastAPI()


