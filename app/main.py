"""
NiceGUI App for Student Management System
Displays lists of students, instructors, and courses from the database.
"""

from nicegui import app, ui
import sys
from pathlib import Path

# Add parent directory to path to import database helpers
sys.path.insert(0, str(Path(__file__).parent.parent))
from database.helpers import (
    get_all_students,
    get_all_instructors,
    get_all_courses,
    authenticate_student,
    get_student_courses_with_details,
    get_student_by_id,
)
from database.database import ensure_database_initialized

ensure_database_initialized()


# Get instructor name by ID (helper function)
def get_instructor_name(instructor_id, instructors_dict):
    """Get instructor full name by ID."""
    instructor = instructors_dict.get(instructor_id)
    if instructor:
        return f"{instructor['FirstName']} {instructor['LastName']}"
    return f"ID: {instructor_id}"


# Create navigation menu for admin
def create_nav():
    """Create navigation menu."""
    with ui.row().classes("w-full justify-center gap-4 p-4 bg-blue-100 shadow-md"):
        ui.button("Students", on_click=lambda: ui.navigate.to("/students")).classes(
            "bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600"
        )
        ui.button(
            "Instructors", on_click=lambda: ui.navigate.to("/instructors")
        ).classes("bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600")
        ui.button("Courses", on_click=lambda: ui.navigate.to("/courses")).classes(
            "bg-purple-500 text-white px-6 py-2 rounded-lg hover:bg-purple-600"
        )


# Login page (root route)
@ui.page("/")
def login_page():
    """Login page for students."""
    ui.page_title("Login - EduTrack")

    with ui.column().classes(
        "flex w-full min-h-screen items-center justify-center bg-gray-100"
    ):
        with ui.card().classes("w-full max-w-md p-8 shadow-lg mx-auto"):
            ui.label("EduTrack").classes(
                "text-4xl font-bold text-center mb-2 text-blue-600"
            )
            ui.label("Student Login").classes("text-xl text-center mb-6 text-gray-600")

            username_input = ui.input(
                "Username", placeholder="Enter your username"
            ).classes("w-full mb-4")
            password_input = ui.input(
                "Password", password=True, placeholder="Enter your password"
            ).classes("w-full mb-4")

            error_container = ui.column().classes("w-full mb-4")

            def show_error(message):
                """Show an error message."""
                error_container.clear()
                with error_container:
                    ui.label(message).classes("text-red-500 text-sm text-center")

            def handle_login():
                error_container.clear()
                username = username_input.value.strip()
                password = password_input.value.strip()

                if not username or not password:
                    show_error("Please enter both username and password.")
                    ui.notify(
                        "Please enter both username and password.", color="negative"
                    )
                    return

                try:
                    student = authenticate_student(username, password)
                    if student:
                        # Store student ID in user session
                        app.storage.user["student_id"] = student["StudentID"]
                        ui.notify(
                            f"Welcome, {student['FirstName']} {student['LastName']}!",
                            color="positive",
                        )
                        ui.navigate.to("/student-dashboard")
                    else:
                        show_error("Invalid username or password. Please try again.")
                        ui.notify(
                            "Invalid username or password. Please try again.",
                            color="negative",
                        )
                except Exception as e:
                    error_msg = f"Login error: {str(e)}"
                    show_error(error_msg)
                    ui.notify(error_msg, color="negative")

            ui.button("Login", on_click=handle_login).classes(
                "w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 mb-4"
            )

            # Allow Enter key to submit
            username_input.on("keydown.enter", handle_login)
            password_input.on("keydown.enter", handle_login)

            ui.separator().classes("my-4")
            ui.label("Admin Access:").classes("text-sm text-gray-500 text-center mb-2")
            ui.button(
                "Admin Dashboard", on_click=lambda: ui.navigate.to("/students")
            ).classes("w-full bg-gray-500 text-white py-2 rounded-lg hover:bg-gray-600")


# Student Dashboard page
@ui.page("/student-dashboard")
def student_dashboard():
    """Student dashboard showing their info and registered courses."""
    ui.page_title("Student Dashboard - EduTrack")

    # Check if student is logged in using user session storage (server-side, persists across pages)
    student_id = app.storage.user.get("student_id")

    if not student_id:
        ui.navigate.to("/")
        return

    try:
        # Get student info
        student = get_student_by_id(student_id)

        if not student:
            ui.navigate.to("/")
            return

        # Header with logout
        with ui.row().classes(
            "w-full justify-between items-center p-4 bg-blue-100 shadow-md"
        ):
            ui.label(f"Welcome, {student['FirstName']} {student['LastName']}").classes(
                "text-xl font-bold text-blue-700"
            )
            ui.button("Logout", on_click=lambda: logout()).classes(
                "bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600"
            )

        def logout():
            if "student_id" in app.storage.user:
                del app.storage.user["student_id"]
            ui.navigate.to("/")

        # Student Information Card
        with ui.card().classes("w-full max-w-4xl mx-auto mt-6 shadow-lg"):
            ui.label("Student Information").classes("text-2xl font-bold mb-4")
            with ui.column().classes("gap-2"):
                ui.label(f"Name: {student['FirstName']} {student['LastName']}").classes(
                    "text-lg"
                )
                ui.label(f"Email: {student['Email']}").classes("text-lg")
                ui.label(f"Student ID: {student['StudentID']}").classes("text-lg")

        # Courses Card
        with ui.card().classes("w-full max-w-4xl mx-auto mt-6 shadow-lg"):
            ui.label("My Registered Courses").classes("text-2xl font-bold mb-4")

            courses_container = ui.column().classes("w-full")

            def load_courses():
                courses_container.clear()

                try:
                    courses = get_student_courses_with_details(student_id)

                    with courses_container:
                        if not courses:
                            ui.label("You are not registered for any courses.").classes(
                                "text-gray-500 p-4"
                            )
                            return

                        # Prepare data for table
                        columns = [
                            {
                                "name": "course_name",
                                "label": "Course Name",
                                "field": "course_name",
                                "sortable": True,
                            },
                            {
                                "name": "credits",
                                "label": "Credits",
                                "field": "credits",
                                "sortable": True,
                                "align": "center",
                            },
                            {
                                "name": "instructor",
                                "label": "Instructor",
                                "field": "instructor",
                                "sortable": True,
                            },
                            {
                                "name": "grade",
                                "label": "Grade",
                                "field": "grade",
                                "align": "center",
                            },
                        ]

                        rows = [
                            {
                                "course_name": c["CourseName"],
                                "credits": c["Credits"],
                                "instructor": c["InstructorName"],
                                "grade": c["Grade"],
                            }
                            for c in courses
                        ]

                        ui.table(columns=columns, rows=rows).classes("w-full")
                        ui.label(f"Total: {len(courses)} courses").classes(
                            "text-sm text-gray-600 mt-4"
                        )

                except Exception as e:
                    with courses_container:
                        ui.label(f"Error loading courses: {str(e)}").classes(
                            "text-red-500 p-4"
                        )

            refresh_button = ui.button(
                "Refresh", icon="refresh", on_click=load_courses
            ).classes("self-end mb-4")
            load_courses()

    except Exception as e:
        ui.label(f"Error: {str(e)}").classes("text-red-500 p-4")


# Students page (Admin)
@ui.page("/students")
def students_page():
    """Display list of all students."""
    ui.page_title("Students - EduTrack")
    create_nav()

    ui.label("Admin Dashboard - Students").classes(
        "text-3xl font-bold text-center mb-6 mt-4 w-full"
    )

    # Create a refreshable container for the table
    with ui.card().classes("w-full max-w-6xl mx-auto shadow-lg"):
        with ui.column().classes("w-full p-4"):
            # Refresh button
            refresh_button = ui.button("Refresh", icon="refresh").classes(
                "self-end mb-4"
            )

            # Container that will hold the table - we'll store a reference to recreate it
            table_area = ui.column().classes("w-full")

            def update_table():
                """Update the students table."""
                # Delete all existing content and recreate
                table_area.clear()

                try:
                    students = get_all_students()

                    # Add new content directly to the cleared container
                    with table_area:
                        if not students:
                            ui.label("No students found.").classes("text-gray-500 p-4")
                            return

                        # Prepare data for table
                        columns = [
                            {
                                "name": "id",
                                "label": "ID",
                                "field": "id",
                                "required": True,
                                "align": "left",
                            },
                            {
                                "name": "first_name",
                                "label": "First Name",
                                "field": "first_name",
                                "sortable": True,
                            },
                            {
                                "name": "last_name",
                                "label": "Last Name",
                                "field": "last_name",
                                "sortable": True,
                            },
                            {"name": "email", "label": "Email", "field": "email"},
                            {
                                "name": "username",
                                "label": "Username",
                                "field": "username",
                                "sortable": True,
                            },
                            {
                                "name": "password",
                                "label": "Password",
                                "field": "password",
                            },
                        ]

                        rows = [
                            {
                                "id": s["StudentID"],
                                "first_name": s["FirstName"],
                                "last_name": s["LastName"],
                                "email": s["Email"],
                                "username": s["Username"],
                                "password": s["Password"],
                            }
                            for s in students
                        ]

                        ui.table(columns=columns, rows=rows, row_key="id").classes(
                            "w-full"
                        )
                        ui.label(f"Total: {len(students)} students").classes(
                            "text-sm text-gray-600 mt-4"
                        )

                except Exception as e:
                    with table_area:
                        ui.label(f"Error loading students: {str(e)}").classes(
                            "text-red-500 p-4"
                        )

            refresh_button.on_click(update_table)
            # Initial load
            update_table()


# Instructors page (Admin)
@ui.page("/instructors")
def instructors_page():
    """Display list of all instructors."""
    ui.page_title("Instructors - EduTrack")
    create_nav()

    ui.label("Admin Dashboard - Instructors").classes(
        "text-3xl font-bold text-center mb-6 mt-4 w-full"
    )

    with ui.card().classes("w-full max-w-6xl mx-auto shadow-lg"):
        with ui.column().classes("w-full p-4"):
            refresh_button = ui.button("Refresh", icon="refresh").classes(
                "self-end mb-4"
            )
            table_area = ui.column().classes("w-full")

            def update_table():
                """Update the instructors table."""
                table_area.clear()

                try:
                    instructors = get_all_instructors()

                    with table_area:
                        if not instructors:
                            ui.label("No instructors found.").classes(
                                "text-gray-500 p-4"
                            )
                            return

                        # Prepare data for table
                        columns = [
                            {
                                "name": "id",
                                "label": "ID",
                                "field": "id",
                                "required": True,
                                "align": "left",
                            },
                            {
                                "name": "first_name",
                                "label": "First Name",
                                "field": "first_name",
                                "sortable": True,
                            },
                            {
                                "name": "last_name",
                                "label": "Last Name",
                                "field": "last_name",
                                "sortable": True,
                            },
                            {
                                "name": "department",
                                "label": "Department",
                                "field": "department",
                                "sortable": True,
                            },
                            {"name": "email", "label": "Email", "field": "email"},
                        ]

                        rows = [
                            {
                                "id": i["InstructorID"],
                                "first_name": i["FirstName"],
                                "last_name": i["LastName"],
                                "department": i["Department"],
                                "email": i["Email"],
                            }
                            for i in instructors
                        ]

                        ui.table(columns=columns, rows=rows, row_key="id").classes(
                            "w-full"
                        )
                        ui.label(f"Total: {len(instructors)} instructors").classes(
                            "text-sm text-gray-600 mt-4"
                        )

                except Exception as e:
                    with table_area:
                        ui.label(f"Error loading instructors: {str(e)}").classes(
                            "text-red-500 p-4"
                        )

            refresh_button.on_click(update_table)
            update_table()


# Courses page (Admin)
@ui.page("/courses")
def courses_page():
    """Display list of all courses."""
    ui.page_title("Courses - EduTrack")
    create_nav()

    ui.label("Admin Dashboard - Courses").classes(
        "text-3xl font-bold text-center mb-6 mt-4 w-full"
    )

    with ui.card().classes("w-full max-w-6xl mx-auto shadow-lg"):
        with ui.column().classes("w-full p-4"):
            refresh_button = ui.button("Refresh", icon="refresh").classes(
                "self-end mb-4"
            )
            table_area = ui.column().classes("w-full")

            def update_table():
                """Update the courses table."""
                table_area.clear()

                try:
                    courses = get_all_courses()
                    instructors = get_all_instructors()

                    # Create a dictionary for quick instructor lookup
                    instructors_dict = {
                        inst["InstructorID"]: inst for inst in instructors
                    }

                    with table_area:
                        if not courses:
                            ui.label("No courses found.").classes("text-gray-500 p-4")
                            return

                        # Prepare data for table
                        columns = [
                            {
                                "name": "id",
                                "label": "ID",
                                "field": "id",
                                "required": True,
                                "align": "left",
                            },
                            {
                                "name": "course_name",
                                "label": "Course Name",
                                "field": "course_name",
                                "sortable": True,
                            },
                            {
                                "name": "credits",
                                "label": "Credits",
                                "field": "credits",
                                "sortable": True,
                                "align": "center",
                            },
                            {
                                "name": "instructor",
                                "label": "Instructor",
                                "field": "instructor",
                                "sortable": True,
                            },
                        ]

                        rows = [
                            {
                                "id": c["CourseID"],
                                "course_name": c["CourseName"],
                                "credits": c["Credits"],
                                "instructor": get_instructor_name(
                                    c["InstructorID"], instructors_dict
                                ),
                            }
                            for c in courses
                        ]

                        ui.table(columns=columns, rows=rows, row_key="id").classes(
                            "w-full"
                        )
                        ui.label(f"Total: {len(courses)} courses").classes(
                            "text-sm text-gray-600 mt-4"
                        )

                except Exception as e:
                    with table_area:
                        ui.label(f"Error loading courses: {str(e)}").classes(
                            "text-red-500 p-4"
                        )

            refresh_button.on_click(update_table)
            update_table()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="EduTrack",
        port=8080,
        reload=False,
        storage_secret="edu-track-student-management-secret-key-2025",
    )
