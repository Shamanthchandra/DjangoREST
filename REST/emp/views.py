from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, mixins
from rest_framework.decorators import api_view


# Create your views here.

class EmployeeList(generics.RetrieveAPIView):
    lookup_field = 'emp_id'
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees1 = Employee.objects.all()
        return employees1

class EmployeePost(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'emp_id'
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    #def put(self, request, *args, **kwargs):
    #   return self.update(request, *args, **kwargs)

    def get_queryset(self):
        qs = Employee.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(emp_id=query)).distinct()
        return qs


class EmployeeUpdateAPIView(mixins.UpdateModelMixin, generics.GenericAPIView):
    lookup_field = 'emp_id'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        return Employee.objects.get(emp_id=self.request.user.id)

class ExampleAllView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer