from rest_framework import serializers
from django.utils import timezone
from apps.users.models import *
from apps.common.models import *
 


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('school_name', 'directory', 'adress')
        
            