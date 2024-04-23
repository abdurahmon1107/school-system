from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('login/', views.LogInView.as_view()),
    path('users/', views.UsersAPIView.as_view()),
]
