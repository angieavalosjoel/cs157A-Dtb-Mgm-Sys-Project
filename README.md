# EduTrack

## Project Overview

This is a EduTrack built with NiceGUI, a Python web framework. The application provides a web-based interface for managing students, instructors, courses, and enrollments. It uses SQLite as the database backend and automatically initializes the database schema and sample data on first run.

## Setup Instructions

### Prerequisites

- Python 3.x (This project was written on Python 3.14 but should run on older versions)

### Installation

1. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

   The main dependency is `nicegui`.

### Running the Application

To start the application, run the following command from the project root directory:

```bash
python app/main.py
```
**Important -** The command must be run from the root directory to resolve python imports

The application will start a web server, and you can access it through your web browser. The default URL is typically `http://localhost:8080` (check the console output for the exact address).

## Dependencies

The project requires:
- **nicegui** - Web framework for building user interfaces with Python

All dependencies are listed in `requirements.txt`. To install them:

```bash
pip install -r requirements.txt
```

### Python Version

This project was written on Python 3.14 but should run on older Python 3.x versions.

## Database Configuration

This project uses SQLite as the database. **No special configuration is needed** - the database will be automatically created and initialized when you first run the application. The database file (`student_management.db`) will be created in the `database` directory if it doesn't already exist.

The application automatically:
- Creates the database schema (tables for students, instructors, courses, and enrollments)
- Populates the database with initial sample data
- Handles all database connections internally

You do not need to manually configure database connections or credentials.
