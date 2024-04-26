from rest_framework import serializers
from django.utils import timezone
from apps.users.models import *
from apps.common.models import *
 
# --------------------------------------------------------------

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
   
    

# -----------------------------------------------------------------------------
class ClassroomSerializer(serializers.ModelSerializer):

    teacher = serializers.SerializerMethodField()
    group = serializers.CharField(source='group.group_name')
    school = serializers.CharField(source='school.school_name')


    class Meta:
        model = ClassRoom
        fields = ('id', 'class_name', 'school', 'capacity', 'group', 'teacher')



    def get_teacher(self, obj):
        return obj.group.teacher.username if obj.group and obj.group.teacher else None
# ---------------------------------------------------------------------------------------------
class ClassRoomListSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.school_name')
    group_name = serializers.CharField(source='group.group_name')
    teacher = serializers.CharField(source='group.teacher.first_name')
    class Meta:
        model = ClassRoom
        fields = ('id', 'class_name', 'school', 'capacity', 'group', 'teacher', 'school_name', 'group_name')
    
# ----------------------------------------------------------------------------------------------
class AttendanceSerializer(serializers.ModelSerializer):
    group = serializers.CharField(source='group.group_name',read_only=True)
    class Meta:
        model = Pupil
        fields = ('id', 'updated_at','group', 'full_name', 'attendance_status')

# --------------------------------------------------------------------------------------------------




class GroupPupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ( 'id','full_name' )



# -------------------------------------------------------------------------------------------------
# maktab qoshish uchun
class AddSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('school_name', 'director', 'adress')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(11111111)
        data['director'] = instance.director.username
        return data


# ------------------------------------------------------------------------------------------------



#maktabga sinf xona qoshish uchun
class AddClasroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('class_name', 'school', 'capacity', 'group')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(instance)
        data['school'] = instance.school.school_name
        data['group'] = instance.group.group_name
        return data

# --------------------------------------------------------------------------------------------------------
# maktabni sinf xonalari royxati    
class SchoolDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('id','class_name', 'group')


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['group'] = instance.group.group_name
        return data
    

class SchoolAbuotSerializers(serializers.ModelSerializer):
    teacher_count = serializers.SerializerMethodField()
    pupils_count = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = ('id','school_name', 'director', 'adress', 'teacher_count', 'pupils_count')
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['director'] = instance.director.first_name
        return data
    def get_teacher_count(self, obj):
        return User.objects.filter(type='Teacher', school_director=obj).count() or 0
        
            


    def get_pupils_count(self, obj):
        print(obj)
        return Pupil.objects.filter(school = obj).count() or 0


class DeleteClassRoom(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        exclude = ['created_at', 'updated_at']