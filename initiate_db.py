from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Define the database URI
DATABASE_URI = "sqlite:///carsite.db"

# Create an engine
engine = create_engine(DATABASE_URI)

# Bind the engine to the Base class's metadata
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create all tables in the database
Base.metadata.create_all(engine)
