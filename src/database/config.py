from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_db():

    db = Session()

    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

