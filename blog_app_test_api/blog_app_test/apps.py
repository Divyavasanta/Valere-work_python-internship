from django.apps import AppConfig

class BlogAppTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app_test'

    def ready(self):
        import blog_app_test.signals
