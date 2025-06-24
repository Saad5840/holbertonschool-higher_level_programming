#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a' from the DB."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine and bind session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with 'a' in their name
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete them one by one
    for state in states_with_a:
        session.delete(state)

    session.commit()
    session.close()
