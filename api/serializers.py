
from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = TODO
        fields = ['id','title','content','created_at','deadline','author']
        # extra_kwargs={'author':{'read_only':True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password']
        extra_kwargs={'password':{'write_only':False}}

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password']
        # extra_kwargs={'password':{'write_only':False}}