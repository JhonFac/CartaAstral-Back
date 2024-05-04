from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .controller import ProcessData
from .email_script import EmailSender
from .models import UserProfile
from .serializers import UserProfileSerializer


class InfoAstral(APIView):

    # def __init__(self):
    #     self.email = EmailSender()

    def get(self, request):
        email = EmailSender()
        email.create_email('est.jbohorquez424@smart.edu.co', 'Jhon Aya', 123)
        data = {
            'message': 'hola'
        }
        return Response(data) 

    def post(self, request):
        process = ProcessData()
        print(request.data)
        serializer = UserProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            _object = serializer.instance
            process.process_email(request.data, _object.id)
            process.crear_carta_astral(_object.nombre_usuario,str(_object.fecha_nacimiento),str(_object.hora_nacimiento),_object.ciudad,_object.longitud,_object.latitud,_object.id,_object.email_usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileCreateView(APIView):
    # permission_classes = [AllowAny]  # Permitir el acceso sin autenticación

    def post(self, request):
        print(request.data)
        serializer = UserProfileSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)