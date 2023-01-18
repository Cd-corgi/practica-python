from django.shortcuts import render
from .serializers import *
from .models import *


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.



class PucApiView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes     = [IsAuthenticated]
    serializer_class         = pucSerializer

    def get(self, request, format=None):
        p = puc.objects.listar_puc()
        return Response(pucSerializer(p, many = True).data)

    def post(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, format=None):
        print(request.data['id'])
        p = puc.objects.get(id=request.data['id'])
        serializer = self.serializer_class(instance = p,data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, format=None):
        pass
