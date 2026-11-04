from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Course
from app.serializers import CourseSerializer
from rest_framework import status

class CourseListCreate(APIView):

    def get(self,request):
        c=Course.objects.all()
        serializer_instance=CourseSerializer(c,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        serializer_instance=CourseSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseRetrieveUpdateDelete(APIView):

    def get(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(c)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        serializer_instance = CourseSerializer(instance=c,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        c = get_object_or_404(Course, id=pk)
        serializer_instance = CourseSerializer(instance=c, data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        c=get_object_or_404(Course,id=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)