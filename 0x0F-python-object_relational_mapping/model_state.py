#!/usr/bin/python3
"""start link class between python and database"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
    """class state for creating table state"""
    __tablename__= 'state'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
