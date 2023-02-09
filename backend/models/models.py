from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)


class Movie(Base):
    __tablename__ = "movie_users"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, index=True)
    owner_id = Column(Integer, index=True)
