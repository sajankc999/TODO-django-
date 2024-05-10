from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.viewsets import generics,ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response
class TodoView(ModelViewSet):
    queryset=TODO.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        return 
    

class RegisterView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        user = authenticate(username = request.data.get('username')
                            ,password=request.data.get('password'))
        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({
                'username':user.get_username(),
                'token': token.key, 
            })
        return Response('User Not Found! Check your credentials')

