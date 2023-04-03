from fastapi import FastAPI

from src.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router.router)

if __name__ == "__main__":
    print("Start")
