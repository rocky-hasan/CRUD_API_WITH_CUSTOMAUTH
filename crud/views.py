from django.shortcuts import render
from rest_framework.parsers import JSONParser
from crud.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from crud.models import Student
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def student_api_list(request):
    if request.method=='GET':
        stu=Student.objects.all()
        serializers=StudentSerializers(stu,many=True)
        return Response(serializers.data)        
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def student_api(request, pk):
    try:
        stu = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializers(stu)
        return Response(serializer.data)

    elif request.method == 'PUT':           # For  UPDATE
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':   # For Delete
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


