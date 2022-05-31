from django.urls import path

import health_check.views as views

urlpatterns = [
    path("", views.health_check),
]
