from fastapi import FastAPI, Body, Depends
from fastapi_users import FastAPIUsers, fastapi_users
from fastapi.middleware.cors import CORSMiddleware

from app.auth.database import User
from app.auth.auth import auth_backend
from app.auth.schemas import UserCreate, UserRead
from app.auth.manager import get_user_manager

# users = []

app = FastAPI(
    title='idky App'
)

origins = [
    "http://79.174.86.5:8000",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://idky-theta.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

# ПРИМЕР
@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"