#!/usr/bin/python3
"""Fetches the State object with the name passed as argument from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Bind the session to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state with the specified name (SQL injection-safe)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
