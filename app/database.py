from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:123456@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Connect to an existing database
# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="123456", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("conn succesfull")
#         break
#     except Exception as Error:
#         print("conn failed")
#         print(Error)
#         time.sleep(2)