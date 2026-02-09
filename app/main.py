from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: Base.metadata.create_all(sync_conn))
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
#app.include_router(?.router)



# health-check endpoint
@app.get("/ping")
async def ping():
    return {"status": "ok"}