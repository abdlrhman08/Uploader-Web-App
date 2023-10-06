from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("uploader/", views.uploader, name="uploader"),
    path("uploader/confirm/", views.confirm, name="confirmation")
]