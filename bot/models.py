import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    tg_id = Column(Integer, unique=True)
    join_date = Column("join_date", DateTime, default=datetime.now())

    def __repr__(self):
        return self.username


class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    breed = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    age_string = Column(String(100), nullable=False)
    personality = Column(String(100), nullable=True)
    description = Column(String(1500), nullable=False)
    special_needs = Column(String(200), nullable=True)
    image_link = Column(String(200), nullable=True)

    def __repr__(self):
        return self.name


class Cat(Base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    breed = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    age_string = Column(String(100), nullable=False)
    personality = Column(String(100), nullable=True)
    description = Column(String(1500), nullable=False)
    special_needs = Column(String(200), nullable=True)
    image_link = Column(String(200), nullable=True)

    def __repr__(self):
        return self.name
