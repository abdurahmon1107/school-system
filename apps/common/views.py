from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics,views
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import *


# maktablar royxati api
class SchoolListAPIView(generics.ListAPIView):
    serializer_class = serializers.SchoolSerializer
    queryset = School.objects.all()
    permission_classes = [IsAuthenticated, IsDerector, IsTeacher]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["region"]
    search_fields = ['school_name']
  



# sinf xona malumotlari
class ClassroomDeteilAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ClassroomSerializer
    queryset = ClassRoom.objects.all()
    lookup_field = 'pk'





#sinf xona listi
class ClassRoomListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClassRoomListSerializer
    queryset = ClassRoom.objects.all()
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['class_name']





# oquvchi davomati keldi-kelmadi
class AttendanceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = serializers.AttendanceSerializer
      # Agar o'quvchini guruh nomi orqali qidirishni istasangiz

    def put(self, request, *args, **kwargs):
        print(request.data)
        return self.update(request, *args, **kwargs)




# sinfni oquvchilari royxati    
class GroupPupilListAPIView(generics.ListAPIView):
    serializer_class = serializers.GroupPupilsSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Pupil.objects.filter(group__id=pk)



# dashboard statistikasi
class StatisticAPIView(views.APIView):
    permission_classes = [IsAuthenticated, IsDerector, IsTeacher]
    def get(self, request):
        pupils_count = Pupil.objects.count()
        school_count = School.objects.count()
        teachers_count = User.objects.filter(type='Teacher').count()
        absent_count = Pupil.objects.filter(attendance_status=KELMADI).count()
        data = {
            'pupils_count':pupils_count,
            'teachers_count':teachers_count,
            'school_count':school_count,
            'absent_count':absent_count,
        }
        return Response(data, status=status.HTTP_200_OK)


# maktab sinfxonalari royxati
    # ----------------------------------------------------------------------------
class SchoolDetailsAPIView(generics.ListAPIView):
    serializer_class = serializers.SchoolDetailsSerializer
    permission_classes = [IsAuthenticated, IsTeacher, IsSchoolDetail]
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return ClassRoom.objects.filter(school__id=pk)





# maktab qoshish
class AddSchoolAPIView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.AddSchoolSerializer


# maktabga sinf xona qoshish

class AddClassRoomAPIView(generics.CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = serializers.AddClasroomSerializer

# 1 ta maktabni hamma malumotlari 

class SchoolAboutAPIView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolAbuotSerializers
    permission_classes = [IsAuthenticated,IsTeacher, IsSchoolDerector]


class DeleteSchoolView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolAbuotSerializers


class DeleteClassRoom(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = serializers.DeleteClassRoom