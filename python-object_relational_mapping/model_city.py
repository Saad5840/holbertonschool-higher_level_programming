#!/usr/bin/python3
"""Defines the City class linked to the 'cities' table in MySQL."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City class linked to the 'cities' table.

    Attributes:
        id (int): primary key, unique, not nullable
        name (str): city name, max 128 chars, not nullable
        state_id (int): foreign key to states.id, not nullable
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Optional: back-reference if you want, but not required here
    # state = relationship("State", back_populates="cities")
