from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from  apimodule.serializer import model_serializer 
from apimodule.models import apiModel
# Create your views here.

class apimoduleview(APIView) :
    
    def get(self, request, format=None) :
        data = apiModel.objects.all()
        serial = model_serializer(data, many = True)
        return Response(serial.data)

    