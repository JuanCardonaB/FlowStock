from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the connection string(DATABASE URL)
connection_string = environ.get("DATABASE_URL")

# Create the engine
engine=create_engine(connection_string)

# Create the session
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create the base class for the models
Base = declarative_base()


try:
  # Print confirmation message
  print("Connection established successfully using SQLAlchemy!")

except Exception as e:
  print("Error connecting to PostgreSQL database:", e)

# activate the venv
# source venv/bin/activate

# command to run the server
#uvicorn app:app --reload 

# commando to run view
# npm run dev or sudo npm run dev

# command to save dependencies
# pip freeze > requirements.txt