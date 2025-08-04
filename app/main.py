from fastapi import FastAPI
from app.config import get_settings
from app import models	# type: ignore
from app import routes
import uvicorn

settings = get_settings()

app = FastAPI()

app.include_router(routes.auth.router, prefix="/auth", tags=["auth"])
app.include_router(routes.protected.router, prefix="/protected", tags=["protected"])


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)