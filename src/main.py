from fastapi import FastAPI

from src.auth import router as auth_router
from src.reception import router as reception_router
from src.service import router as service_router

app = FastAPI(
    title="dentist office"
)

app.include_router(auth_router.router)
app.include_router(reception_router.router)
app.include_router(service_router.router)

if __name__ == "__main__":
    print("Start app")
