import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host='79.174.86.5', port=8000, reload=True)
#
# from fastapi import FastAPI, Body, Depends
# from fastapi_users import FastAPIUsers, fastapi_users
#
# from app.auth.database import User
# from app.auth.auth import auth_backend
# from app.auth.schemas import UserCreate, UserRead
# from app.auth.manager import get_user_manager
#
# # users = []
#
# app = FastAPI(
#     title='idky App'
# )
#
# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )
#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )
#
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )