from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv

load_dotenv()

connection_string = environ.get("DATABASE_URL")

engine=create_engine(connection_string)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


try:
  # Print confirmation message
  print("Connection established successfully using SQLAlchemy!")

except Exception as e:
  print("Error connecting to PostgreSQL database:", e)

