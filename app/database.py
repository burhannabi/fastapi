from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

engine = create_engine(f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}")
print(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="baba786.",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Database connection was successfull")
#         break
#     except Exception as e:
#         print(f"Connection to database failed: {e}")
#         time.sleeep(2)
