from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.main import app


@app.get("/accounts")
async def get_accounts(
        db: Session = Depends(get_db)  # получаем готовую сессию
):
    accounts = db.get()

    return accounts