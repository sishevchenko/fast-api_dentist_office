from fastapi import Depends
from fastapi import APIRouter

from src.auth import config as auth_config
from src.auth import schemas as auth_schemas
from src.auth import models as auth_models

router = APIRouter()

router.include_router(
    auth_config.fastapi_users.get_auth_router(auth_config.auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

router.include_router(
    auth_config.fastapi_users.get_register_router(auth_schemas.UserRead, auth_schemas.UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    auth_config.fastapi_users.get_verify_router(auth_schemas.UserRead),
    prefix="/auth",
    tags=["Auth"],
)
