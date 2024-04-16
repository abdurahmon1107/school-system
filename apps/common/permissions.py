from rest_framework.permissions import BasePermission
from .models import *

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return not request.user.type == "Teacher"


class IsDerector(BasePermission):
    def has_permission(self, request, view):
        print(request.user.type)
        return not request.user.type == "Director"
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user.type)
        return request.user.type == "Admin"

class IsSchoolDerector(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.director.id == request.user.id or request.user.type == 'Admin'


class IsSchoolDetail(BasePermission):
    def has_permission(self, request, view):
        url_pk = view.kwargs.get('pk')
        school = School.objects.get(pk=url_pk)
        return request.user.id == school.director.id  or request.user.type == 'Admin'