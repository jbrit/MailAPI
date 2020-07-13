from rest_framework import serializers
from .models import EmailAdded, Profile, User
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['email_list']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class EmailAddedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmailAdded
        fields = ["id","email"]