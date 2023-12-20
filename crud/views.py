from django.shortcuts import render
from crud.serializers import StudentSerializers
from crud.models import Student
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from rest_framework.reverse import reverse


# Create your views here.
#class Student_api_list(mixins.ListModelMixin,mixins.CreateModelMixin): or use (generics.ListCreateAPIView)
class Student_api_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

# class Student_detail(generics.RetrieveUpdateDestroyAPIView) if use this dont need mixins
class Student_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs )

    def delete(self, request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)









# class Student_api_list(APIView):
#     def get(self,request,format=None):
#         stu=Student.objects.all()
#         serializers=StudentSerializers(stu,many=True)
#         return Response(serializers.data)        
#     def post(self,request,format=None):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class Student_detail(APIView):
#     def get_objects(self,pk):
#         try:
#             stu = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk, format=None):
#         serializer = self.get_object(pk)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):          # For  UPDATE
#         stu = self.get_objects(pk)
#         serializer=StudentSerializers(stu,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk,format=None):  # For Delete
#         stu=self.get_objects(pk)
#         stu.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


