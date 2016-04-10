from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fishes.models import Fish
from fishes.serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
	#this will fetch all the rows of data in the Fish table
	queryset = Fish.objects.all()
	serializer_class = FishSerializer



#running the url http://127.0.0.1:8000/api/fishes/ 
# you will be able to view the browsable API
