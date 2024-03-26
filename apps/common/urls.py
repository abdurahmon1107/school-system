from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("schools_list/", views.SchoolListAPIView.as_view()),
    path("classroom/<int:pk>", views.ClassroomDeteilAPIView.as_view()),
]
