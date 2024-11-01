from django.apps import AppConfig


class SampleAppConfig(AppConfig):
    name = "tests.sample_app"
    app_label = "sample_app"
    default_auto_field = "django.db.models.AutoField"
