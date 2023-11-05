from django.apps import AppConfig


class ProductConfig(AppConfig):
    """
    This class allows certain configurations for the primary app in the Django project, the product app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
