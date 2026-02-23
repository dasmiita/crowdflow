from rest_framework import serializers
from .models import TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    available_spots = serializers.SerializerMethodField()

    class Meta:
        model = TimeSlot
        fields = ['id', 'date', 'start_time', 'end_time', 'capacity', 'booked_count', 'available_spots']

    def get_available_spots(self, obj):
        return obj.capacity - obj.booked_count