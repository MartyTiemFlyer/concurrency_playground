from sqlalchemy import Boolean, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Модель
class File_model(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, index=True)