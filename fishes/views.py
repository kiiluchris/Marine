from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from fishes.models import Fish
from fishes.serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
	#this will fetch all the rows of data in the fish table
	queryset = Fish.objects.all()
	serializer_class = FishSerializer

