#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Create a configured "Session" class and an instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add new State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the ID of the new state
    print(new_state.id)

    session.close()
