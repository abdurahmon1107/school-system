from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics,views
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import serializers
from apps.common.permissions import *
from .models import User

class LogInView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated,IsAdminUser,IsAdmin]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['username']
    filterset_fields = ['type']


    