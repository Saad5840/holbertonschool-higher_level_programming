#!/usr/bin/python3
"""Updates the name of the State object with id = 2 to 'New Mexico'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create the engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Create a configured "Session" class and instantiate a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the State with id=2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update its name if found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
