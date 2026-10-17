
import sqlite3
from contextlib import contextmanager


@contextmanager
def get_connection(database_path):
    """Open a database connection and always close it afterward."""
    connection = sqlite3.connect(database_path)

    try:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")

        yield connection

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def init_db(database_path):
    """Create the applications table if it does not exist."""
    with get_connection(database_path) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                job_role TEXT NOT NULL,
                application_date TEXT NOT NULL,
                status TEXT NOT NULL CHECK (
                    status IN (
                        'Applied',
                        'Online Assessment',
                        'Interview',
                        'Selected',
                        'Rejected'
                    )
                ),
                job_url TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                follow_up_date TEXT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
