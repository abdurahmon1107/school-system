from rest_framework import serializers
from django.utils import timezone
from apps.users.models import *
from apps.common.models import *
 


class SchoolSerializer(serializers.ModelSerializer):

    teacher_count = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()
    director = serializers.CharField(source='director.first_name')

    class Meta:
        model = School
        fields = ('id', 'school_name', 'director', 'adress', 'teacher_count', 'pupils_count')
    def get_teacher_count(self, obj):
        return User.objects.filter(type='Teacher', school_director=obj).count()
            


    def get_pupils_count(self, obj):
        return User.objects.filter(type='Pupil', school_director=obj).count()


class ClassroomSerializer(serializers.ModelSerializer):

    teacher = serializers.SerializerMethodField()


    class Meta:
        model = ClassRoom
        fields = ('id', 'class_name', 'school', 'capacity', 'group', 'teacher')



    def get_teacher(self, obj):
        return obj.group.teacher.username if obj.group and obj.group.teacher else None

class ClassRoomListSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.school_name')
    group = serializers.CharField(source='group.group_name')
    class Meta:
        model = ClassRoom
        fields = ('id', 'class_name', 'school', 'capacity', 'group')
    