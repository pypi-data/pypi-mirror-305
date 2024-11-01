from django.conf import settings
import logging

def check_celery():
    from celery import Celery
    from kombu import Connection
    try:
        project_name = settings.SETTINGS_MODULE.split('.')[0]
        # Initialize Celery with the broker URL
        app = Celery(project_name, broker=settings.CELERY_BROKER_URL)
        
        # Test the connection to the broker directly
        with Connection(settings.CELERY_BROKER_URL) as conn:
            conn.connect()
        logging.info("Celery broker is reachable")
        return True, "Celery broker is reachable"
    except Exception as e:
        logging.error(f"Celery broker health check failed: {str(e)}")
        return False, f"Celery broker error: {str(e)}"
