from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics,views
from . import serializers
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SchoolListAPIView(generics.ListAPIView):
    serializer_class = serializers.SchoolSerializer
    queryset = School.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['school_name']
  


class ClassroomDeteilAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ClassroomSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'pk'


class ClassRoomListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClassRoomListSerializer
    queryset = ClassRoom.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['class_name']
