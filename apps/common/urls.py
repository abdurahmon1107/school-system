from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("schools_list/", views.SchoolListAPIView.as_view()),
    path("classroom/<int:pk>", views.ClassroomDeteilAPIView.as_view()),
    path("classroom-list/", views.ClassRoomListAPIView.as_view()),
    path("attendance-page/<int:pk>/", views.AttendanceRetrieveUpdateAPIView.as_view()),
    path("group-pupil-list/<int:pk>/", views.GroupPupilListAPIView.as_view()),
    path('dashboard/', views.StatisticAPIView.as_view()),
]
