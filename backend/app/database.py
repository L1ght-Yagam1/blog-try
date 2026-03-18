import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, text


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def check_db():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ DB connection OK")
    except Exception as e:
        print("❌ DB connection FAILED:", e)

