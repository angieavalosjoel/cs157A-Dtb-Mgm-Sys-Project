# HELPER FUNCTIONS 

def get_session():
    return SessionLocal()

# STUDENT HELPERS

def get_all_students():
    with get_session() as session:
        return session.query(Student).all()

def add_student(first_name, last_name, email):
    with get_session() as session:
        s = Student(FirstName=first_name, LastName=last_name, Email=email)
        session.add(s)
        session.commit()

def update_student(student_id, first_name, last_name, email):
    with get_session() as session:
        s = session.query(Student).get(student_id)
        if s:
            s.FirstName = first_name
            s.LastName = last_name
            s.Email = email
            session.commit()

def delete_student(student_id):
    with get_session() as session:
        s = session.query(Student).get(student_id)
        if s:
            session.delete(s)
            session.commit()

# INSTRUCTOR HELPERS

def get_all_instructors():
    with get_session() as session:
        return session.query(Instructor).all()

def add_instructor(first_name, last_name, department, email):
    with get_session() as session:
        inst = Instructor(
            FirstName=first_name,
            LastName=last_name,
            Department=department,
            Email=email
        )
        session.add(inst)
        session.commit()

# COURSE HELPERS

def get_all_courses():
    with get_session() as session:
        return session.query(Course).all()

def add_course(name, credits, instructor_id):
    with get_session() as session:
        c = Course(CourseName=name, Credits=credits, InstructorID=instructor_id)
        session.add(c)
        session.commit()

def delete_course(course_id):
    with get_session() as session:
        c = session.query(Course).get(course_id)
        if c:
            session.delete(c)
            session.commit()

# ENROLLMENT HELPERS

def get_all_enrollments():
    with get_session() as session:
        return session.query(Enrollment).all()

def enroll_student(student_id, course_id):
    with get_session() as session:
        e = Enrollment(StudentID=student_id, CourseID=course_id, Grade="IP")
        session.add(e)
        session.commit()

def update_grade(enrollment_id, grade):
    with get_session() as session:
        e = session.query(Enrollment).get(enrollment_id)
        if e:
            e.Grade = grade
            session.commit()

def get_student_enrollments(student_id):
    with get_session() as session:
        return (
            session.query(Enrollment)
            .filter(Enrollment.StudentID == student_id)
            .all()
        )
