from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from src.auth import router as auth_router
from src.reception import router as reception_router
from src.service import router as service_router

app = FastAPI(
    title="dentist office"
)

app.include_router(auth_router.router)
app.include_router(reception_router.router)
app.include_router(service_router.router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    print("Start app")
