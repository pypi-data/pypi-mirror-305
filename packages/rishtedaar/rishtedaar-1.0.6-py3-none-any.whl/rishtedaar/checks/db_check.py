from django.db import connection
import logging

def check_db():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()  # Fetch results to ensure the query executes
        logging.info("Database connection is healthy")
        return True, "Database connection is healthy"
    except Exception as e:
        logging.error(f"Database health check failed: {str(e)}")
        return False, f"Database error: {str(e)}"
