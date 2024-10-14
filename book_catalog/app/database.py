from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://my_database_bsvc_user:REiLBxSM1rtGv3wPF3UDVzRzx31N4zkU@dpg-cs6freqj1k6c73a30b3g-a.singapore-postgres.render.com/my_database_bsvc" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
