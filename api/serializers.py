from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import Token







class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']
    
    

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password']
        
        
        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}
        
    
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user