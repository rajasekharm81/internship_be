from shared.database.database import Base
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, UniqueConstraint, ForeignKey, Time, Sequence, Text, CheckConstraint
from datetime import datetime


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(100))
    is_active = Column(Integer,default=1)
