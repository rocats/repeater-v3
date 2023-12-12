from fastapi import FastAPI
from uvicorn import run

from api.v1.router import router

app = FastAPI()
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    run("index:app", host="0.0.0.0", port=5000, reload=True, workers=1)
