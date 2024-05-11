from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.viewsets import generics,ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class TodoView(ModelViewSet):
    
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        return TODO.objects.filter(author=user)
    
    

class RegisterView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    def create(self,request):  
        username = request.data.get('username')
        password = request.data.get('password')


        if User.objects.filter(username=username).exists():
            return Response({"message":"user exists"})
        else:
            user=User.objects.create_user(username=username,password=password)
            token ,_ = Token.objects.get_or_create(user=user)
            return Response({
                "status":"created",
                "username":user.get_username(),
                "token":token.key,
            })

class loginViewset(APIView):
    def post(self,request):
        try:
            username=request.data.get("username")
            password=request.data.get("password")
            serializer = UserLoginSerializer(data = request.data)
            # if not serializer.is_valid():
            #     return Response({
            #         "message":serializer.errors,
            #         })
            # serializer.save()
            user = authenticate(username=username,password = password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                return Response({
                    "username":user.get_username(),
                    "token":token.key,                    
                })
            return Response("no user found")
        except Exception as e:
            return Response({"error":e,})
