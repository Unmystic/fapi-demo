from fastapi import FastAPI
from src.books.routes import router
from contextlib import asynccontextmanager
from src.db.main import initdb


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initdb()
    yield
    print("Server is stopping")


version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=lifespan,
)

app.include_router(router, prefix=f"/api/{version}/books", tags=["books"])
