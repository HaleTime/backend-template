from fastapi import FastAPI
from app.api.main import api_router
from app.core.db import async_engine
from sqlmodel import SQLModel


class MyApp(FastAPI):
    pass


def create_app():
    my_app = MyApp(openapi_url=None, docs_url=None, redoc_url=None)
    init_app(my_app)
    return my_app


def init_app(my_app):
    my_app.include_router(api_router)


app = create_app()


@app.on_event("startup")
async def on_startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
