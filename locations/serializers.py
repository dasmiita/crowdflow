from rest_framework import serializers
from .models import Temple

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = ['id', 'name', 'city', 'address', 'description', 'daily_capacity']