from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields =  "__all__"
        # extra_kwargs = {'author':{'write_only':True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password']
        extra_kwargs={'password':{'write_only':False}}