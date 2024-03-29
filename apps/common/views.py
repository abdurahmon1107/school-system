from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics,views
from . import serializers
from .models import *

class SchoolListAPIView(generics.ListAPIView):
    serializer_class = serializers.SchoolSerializer
    queryset = School.objects.all()
   
   
    # serializer_class = serializers.SchoolSerializer

    # def get(self , request , format=None):
    #         school = School.objects.all()
    #         school_name = school['school_name']
    #         directory = school['directory']
    #         adress = school['adress']
    #         teacher_count = 0
    #         pupil_count = Pupil.objects.count()
    #         for user in User.objects.all():
    #             if user.type == 'Teacher':
    #                 teacher_count += 1
                
    #         data = {
    #           'school_name': school_name,
    #             'directory': directory,
    #             'adress': adress,
    #             'teacher_count': teacher_count,
    #             'pupil_count': pupil_count
    #         }
    #         return Response(data, status=status.HTTP_200_OK)    


class ClassroomDeteilAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ClassroomSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'pk'

class ClassRoomListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClassroomSerializer
    queryset = ClassRoom.objects.all()
    