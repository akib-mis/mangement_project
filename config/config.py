from sqlalchemy import create_engine
from typing import Generator
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from config.db import DATABASE_URL

Base: DeclarativeMeta = declarative_base()

engine = create_engine(
    DATABASE_URL
)
session_maker = sessionmaker(autocommit=False,expire_on_commit = False ,autoflush=False, bind=engine)

def get_db_session() -> Generator[Session,None,None]:
    db = session_maker()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    with engine.begin() as conn:
        # conn.run_sync(Base.metadata.create_all)
        Base.metadata.create_all(bind=engine)