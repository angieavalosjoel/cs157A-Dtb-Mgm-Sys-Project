import sqlite3
import os

# os.path.join(os.path.dirname(__file__), "name_of_file")
# Standard way of getting absolute path

DATABASE_URL = os.path.join(os.path.dirname(__file__), "student_management.db")


def get_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn


def database_exists():
    """Check if the database file exists."""
    return os.path.exists(DATABASE_URL)


def recreate_tables():
    """Execute create_schema.sql to create database tables"""
    conn = get_connection()
    cursor = conn.cursor()

    schema_file = os.path.join(os.path.dirname(__file__), "create_schema.sql")
    with open(schema_file, "r", encoding="utf-8") as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)

    conn.commit()
    conn.close()


def initialize_data():
    """Execute initialize_data.sql to populate database"""
    conn = get_connection()
    cursor = conn.cursor()

    init_file = os.path.join(os.path.dirname(__file__), "initialize_data.sql")
    with open(init_file, "r", encoding="utf-8") as f:
        init_sql = f.read()
        cursor.executescript(init_sql)

    conn.commit()
    conn.close()


def ensure_database_initialized():
    """Check if database is missing, and if so, create and populate it.
    Returns True if database was initialized, False if it already existed.
    """
    if not database_exists():
        recreate_tables()
        initialize_data()
        return True
    return False
