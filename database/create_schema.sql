-- Database Schema for Student Management System

-- Drop tables
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;

-- Instructors table
CREATE TABLE instructors (
    InstructorID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Department TEXT NOT NULL,
    Email TEXT NOT NULL
);

-- Students table
CREATE TABLE students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL
);

-- Courses table
CREATE TABLE courses (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
    CourseName TEXT NOT NULL,
    Credits INTEGER NOT NULL,
    InstructorID INTEGER NOT NULL,
    FOREIGN KEY (InstructorID) REFERENCES instructors(InstructorID)
);

-- Enrollments table
CREATE TABLE enrollments (
    EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER NOT NULL,
    CourseID INTEGER NOT NULL,
    Grade TEXT NOT NULL DEFAULT 'IP',
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
);




