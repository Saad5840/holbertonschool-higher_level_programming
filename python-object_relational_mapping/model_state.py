#!/usr/bin/python3
"""Defines the State class mapped to the states table in MySQL."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a Base instance for the ORM to work with
Base = declarative_base()


class State(Base):
    """Represents a state in the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
