from django.contrib import admin
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured

app_label = __package__.split('.')[0]

try:
    app_config = apps.get_app_config(app_label)
except ImproperlyConfigured:

    app_config = None

if app_config:
    for model in app_config.get_models():
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass