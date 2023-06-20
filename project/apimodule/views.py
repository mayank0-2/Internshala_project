from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics

from apimodule.models import apiModel
from apimodule.serializer import model_serializer, UserRegistrationSerializer


# Create your views here.

class apimoduleview(APIView) :
    
    def get(self, request, format=None) : 
        data = apiModel.objects.all()
        serial = model_serializer(data, many = True)
        return Response(serial.data)
    
    
    def post(self, request, format=None) :
        serial = model_serializer(data = request.data)
        if serial.is_valid():
            print('working')
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            print('Not working fine')
            return Response(serial.errors) 
    
    
    def put(self, request, id, format = None) :
        try:
            instance = apiModel.objects.get(id=id)
            serial = model_serializer(instance, data = request.data, partial = True)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            else :
                return Response(serial.errors)     
        except:
            return Response(status.HTTP_204_NO_CONTENT) 
    
    def delete(self, request, id, format = None) :
        permission_classes=[IsAdminUser]
        
        instance = apiModel.objects.get(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
    
class UserRegistrationView(APIView):
    
    permission_classes=[IsAdminUser]
    
    def post(self, request):
        serial = UserRegistrationSerializer(data = request.data)
        if serial.is_valid() :
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(serial.errors)