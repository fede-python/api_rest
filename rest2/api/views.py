from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import student
from .serializers import studenserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

@api_view(["GET","POST"])
def show_list(request):
    if (request.method=="GET"):
        data = student.objects.all()
        serial = studenserializers(data,many=True)
        return Response(serial.data)
    elif (request.method=="POST"):
        serial=studenserializers(data=request.data)
        if (serial.is_valid()):
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
