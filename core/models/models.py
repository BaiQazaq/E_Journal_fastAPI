from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    scores = relationship("Score", back_populates="student", cascade="all, delete-orphan")

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="scores")
