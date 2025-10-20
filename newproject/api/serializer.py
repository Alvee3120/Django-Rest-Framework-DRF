from rest_framework import serializers
from .models import DB_USER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB_USER
        fields = '__all__'