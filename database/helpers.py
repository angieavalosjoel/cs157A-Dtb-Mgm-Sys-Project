# Helper functions
from database.database import get_connection


# Students
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    # Converting to dictionary makes it easier
    return [dict(row) for row in rows]


def add_student(first_name, last_name, email, username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (FirstName, LastName, Email, Username, Password) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, email, username, password),
    )
    conn.commit()
    conn.close()


def update_student(student_id, first_name, last_name, email, username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET FirstName = ?, LastName = ?, Email = ?, Username = ?, Password = ? WHERE StudentID = ?",
        (first_name, last_name, email, username, password, student_id),
    )
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE StudentID = ?", (student_id,))
    conn.commit()
    conn.close()


# Instructors
def get_all_instructors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM instructors")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_instructor(first_name, last_name, department, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO instructors (FirstName, LastName, Department, Email) VALUES (?, ?, ?, ?)",
        (first_name, last_name, department, email),
    )
    conn.commit()
    conn.close()


# Courses
def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_course(name, credits, instructor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (CourseName, Credits, InstructorID) VALUES (?, ?, ?)",
        (name, credits, instructor_id),
    )
    conn.commit()
    conn.close()


def delete_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE CourseID = ?", (course_id,))
    conn.commit()
    conn.close()


# Enrollments
def get_all_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enrollments")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO enrollments (StudentID, CourseID, Grade) VALUES (?, ?, ?)",
        (student_id, course_id, "IP"),
    )
    conn.commit()
    conn.close()


def update_grade(enrollment_id, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE enrollments SET Grade = ? WHERE EnrollmentID = ?",
        (grade, enrollment_id),
    )
    conn.commit()
    conn.close()


def get_student_enrollments(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enrollments WHERE StudentID = ?", (student_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def authenticate_student(username, password):
    """Authenticate a student by username and password. Returns student dict if successful, None otherwise."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE Username = ? AND Password = ?",
        (username, password),
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_student_by_id(student_id):
    """Get a student by their ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE StudentID = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_student_courses_with_details(student_id):
    """Get all courses a student is enrolled in with course details."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT 
            e.EnrollmentID,
            e.Grade,
            c.CourseID,
            c.CourseName,
            c.Credits,
            c.InstructorID,
            i.FirstName || ' ' || i.LastName AS InstructorName
        FROM enrollments e
        JOIN courses c ON e.CourseID = c.CourseID
        JOIN instructors i ON c.InstructorID = i.InstructorID
        WHERE e.StudentID = ?
        ORDER BY c.CourseName
    """,
        (student_id,),
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
