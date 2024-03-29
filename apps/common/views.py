from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics,views
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication

class SchoolListAPIView(generics.ListAPIView):
    serializer_class = serializers.SchoolSerializer
    queryset = School.objects.all()
  


class ClassroomDeteilAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ClassroomSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'pk'


class ClassRoomListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClassRoomListSerializer
    queryset = ClassRoom.objects.all()