from django.urls import path
from .views import home_page, personal_view

urlpatterns = [
    path("", home_page, name='home'),
    path("header", personal_view, name='header')
]
