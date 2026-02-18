from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Company, Application
from .serializers import CompanySerializer, ApplicationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by("name")
    serializer_class = CompanySerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related("company").all().order_by("-updated_at")
    serializer_class = ApplicationSerializer
