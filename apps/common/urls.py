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
    path('add-school/', views.AddSchoolAPIView.as_view()),
    path('school-details/<int:pk>/', views.SchoolDetailsAPIView.as_view()),
    path('add-classroom/', views.AddClassRoomAPIView.as_view()),
    path('school-about/<int:pk>/', views.SchoolAboutAPIView.as_view()),
    path('delete-school/<int:pk>', views.DeleteSchoolView.as_view()),
    path('delete-classroom/<int:pk>', views.DeleteClassRoom.as_view()),
]
