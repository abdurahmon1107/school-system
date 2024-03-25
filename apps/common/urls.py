from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path('school_list', views.SchoolListAPIView.as_view()),
]
