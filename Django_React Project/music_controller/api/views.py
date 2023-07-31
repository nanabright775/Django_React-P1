from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializers
from .models import Room
#create your views here

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers