from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class InfoAstral(APIView):

    def get(self, request):
        data = {
            'message': 'hola'
        }
        return Response(data) 
