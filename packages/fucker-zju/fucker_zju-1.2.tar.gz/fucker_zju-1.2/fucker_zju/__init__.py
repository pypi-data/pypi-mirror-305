import mimetypes
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)

from .celery import app as celery_app
__all__ = ('celery_app',)