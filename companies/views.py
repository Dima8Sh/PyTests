from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializer import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer

