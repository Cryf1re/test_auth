from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.protected import router as protected_router
import uvicorn

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(protected_router, prefix="/protected", tags=["protected"])


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)