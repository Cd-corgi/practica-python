from django.shortcuts import render
# Create your views here.

from django.views.generic import (
    CreateView
)

from django.contrib.auth import authenticate,login,logout
from apps.users.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser,ParseError
from rest_framework.exceptions import NotFound,PermissionDenied
from rest_framework.generics import (CreateAPIView, ListAPIView,)
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

from .serializers import (LoginTradicionalSerializers,UserListSerializers)

# from apps.acceso.serializers import (permisosSerializer)

# from apps.acceso.models import (permisos_model)

class tradicionalLoginView(APIView):
    parser_classes   = (JSONParser,)
    serializer_class = LoginTradicionalSerializers
    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        correo   = serializer.data.get('correo')
        password = serializer.data.get('password')

        print(correo+' '+password)
        user = authenticate(
            email = correo,
            password = password
        )
        print(user)
        if not user:
            raise PermissionDenied('Por favor introduzca el email y la clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas.')
        login(self.request, user)
        token = ""
        try:
            token = Token.objects.get(user = user)
        except Token.DoesNotExist:
            token = Token.objects.create(user = user)


        
        user = UserListSerializers(user)
        # permisos = permisos_model.objects.get(usuario = self.request.user.id)

        return Response(
            {
                'token': token.key,
                'user': user.data,
                # 'permisos': permisosSerializer(permisos).data,
            }
        )

class UserAPIListView(ListAPIView):
	# authentication_classes = [TokenAuthentication]
	# permission_classes     = [IsAuthenticated]
	serializer_class       = UserListSerializers

	def get_queryset(self):
		return User.objects.all()



class LogoutApiView(APIView): 
    def get(self,request,format=None):
        logout(request)
        
        return Response(
            {
                'result': True,
            }
        )
    