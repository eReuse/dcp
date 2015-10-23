from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Place
from .serializers import PlaceSerializer


class PlaceView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (IsAdminUser,)
