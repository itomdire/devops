from django.contrib import admin
from django.urls import path

from users.views import (
    health_check,
    register,
    login,
    me,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/health/",
        health_check
    ),

    path(
        "api/auth/register/",
        register
    ),

    path(
        "api/auth/login/",
        login
    ),

    path(
        "api/auth/me/",
        me
    ),
]