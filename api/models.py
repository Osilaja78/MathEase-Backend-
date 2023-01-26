from sqlalchemy import Column ,String, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from .database import Base

# This model stores users info
class User(Base):
    __tablename__ = "Users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_verified = Column(Boolean, default=False)

    question_history = relationship("QuestionHistory", back_populates="author")

# This model stores history of questions asked by users
class QuestionHistory(Base):
    __tablename__ = "QuestionHistorys"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    author_id = Column(String, ForeignKey('Users.id'))
    date_created = Column(DateTime(timezone=True))

    author = relationship("User", back_populates="question_history")

# Password reset model
class PasswordReset(Base):
    __tablename__ = "PasswordReset"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    code = Column(String)
    date_created = Column(DateTime(timezone=True))