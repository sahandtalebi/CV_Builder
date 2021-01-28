from django.urls import path
from .views import BlogList, DetailPost


urlpatterns = [
    path('blog', BlogList.as_view(), name='blog'),
    path('blog/<int:pk>', DetailPost.as_view())
]