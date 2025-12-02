from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

#DATABASE SETUP 

# SQLite database file
DATABASE_URL = "sqlite:///student_management.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

#MODELS

class Student(Base):
    __tablename__ = "students"

    StudentID = Column(Integer, primary_key=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Email = Column(String, nullable=False)

    enrollments = relationship("Enrollment", back_populates="student")

class Instructor(Base):
    __tablename__ = "instructors"

    InstructorID = Column(Integer, primary_key=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Department = Column(String, nullable=False)
    Email = Column(String, nullable=False)

    courses = relationship("Course", back_populates="instructor")

class Course(Base):
    __tablename__ = "courses"

    CourseID = Column(Integer, primary_key=True)
    CourseName = Column(String, nullable=False)
    Credits = Column(Integer, nullable=False)
    InstructorID = Column(Integer, ForeignKey("instructors.InstructorID"), nullable=False)

    instructor = relationship("Instructor", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

class Enrollment(Base):
    __tablename__ = "enrollments"

    EnrollmentID = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey("students.StudentID"), nullable=False)
    CourseID = Column(Integer, ForeignKey("courses.CourseID"), nullable=False)
    # Grade is NOT NULL, default "IP" (In Progress) to satisfy "no null fields"
    Grade = Column(String, nullable=False, default="IP")

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

#CREATE TABLES

Base.metadata.create_all(engine)

#SEED DATA (15+ PER TABLE)
#add data automatically to resemble real data
def seed_data():
    session = SessionLocal()

    # seed if tables are empty
    if session.query(Student).count() == 0:
        students = [
            Student(FirstName=f"Student{i}", LastName="Test", Email=f"student{i}@school.edu")
            for i in range(1, 16)
        ]
        session.add_all(students)
    # seed instructors
    if session.query(Instructor).count() == 0:
        instructors = [
            Instructor(
                FirstName=f"Instructor{i}",
                LastName="Last",
                Department="CS",
                Email=f"instructor{i}@school.edu"
            )
            for i in range(1, 16)
        ]
        session.add_all(instructors)

    #seed courses
    if session.query(Course).count() == 0:
        # Tie first 10 courses to first 10 instructors
        courses = [
            Course(
                CourseName=f"CS{i:03d}",
                Credits=3 + (i % 2),
                InstructorID=i  # assumes InstructorID 1-15
            )
            for i in range(1, 16)
        ]
        session.add_all(courses)
        
    # seed enrollments
    if session.query(Enrollment).count() == 0:
        enrollments = []
        # first 10 students each take first 5 courses
        for student_id in range(1, 11):
            for course_id in range(1, 6):
                enrollments.append(
                    Enrollment(
                        StudentID=student_id,
                        CourseID=course_id,
                        Grade="IP"  
                    )
                )
        session.add_all(enrollments)

    session.commit()
    session.close()

seed_data()

print("Database and seed data ready.")
