from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

sys.path.append('.')
# custom imports

connection_string = 'mysql+mysqlconnector://raja:1234@127.0.0.1:3306/internship'

engine = create_engine(
    connection_string
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
