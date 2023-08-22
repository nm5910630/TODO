from rest_framework import serializers
from .models import TODO

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
