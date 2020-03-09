from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from .serializers import employeeSerializer
from rest_framework import generics


class employeeList(generics.ListAPIView):

    #def get(self,request):
    employees = employee.objects.all()
    serializer_class = employeeSerializer(employees, many=True)
        #return Response(serializer.data)

    def get_queryset(self):
        queryset=employee.objects.all()
        var=self.request.query_params.get("first_name","")
        return queryset.filter(first_name=var)
