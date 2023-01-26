from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL for sqlite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./mathEase.db"

# Create SQLAlcheny engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

#  Create a sessionLocal class
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Creata a base class
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()