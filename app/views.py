from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        qset = students.objects.all()
        serializer = studentsSerializer(qset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        id = pk
        if id is not None:
            stu = students.objects.get(pk=id)
            serializer = studentsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = studentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        id = pk
        if id is not None:
            stu = students.objects.get(id= id)
            serializer = studentsSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, pk):
        id = pk
        if id is not None:
            stu = students.objects.get(id= id)
            serializer = studentsSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated'},status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        if id is not None:
            stu = students.objects.get(id= id)
            stu.delete()
            return Response({'msg':'Data Deleted'},status=status.HTTP_201_CREATED)




# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = students.objects.all()
#     serializer_class = studentsSerializer

# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = students.objects.all()
#     serializer_class = studentsSerializer
