from rest_framework import serializers
from django.utils import timezone
from apps.users.models import *
from apps.common.models import *


class LoginSerializer(serializers.Serializer):
    TURLAR = (
        ('Teacher', 'Teacher'),
        ('Director', 'Director'),
        ('Admin', 'Admin')
    )
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    type = serializers.ChoiceField(choices=TURLAR)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        type = attrs['type']

        user = User.objects.filter(username=username).first()
        print(attrs)
        print(user)
        if not user:
            raise serializers.ValidationError({"msg": "User does not exist!"})

        if not type == user.type:
            raise serializers.ValidationError({"msg":"User not found"})
        

        if not user.check_password(password):
            raise serializers.ValidationError({"msg": "Password does not match"})
        
        self.instance = user
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.tokens()
        return data
    

   
        