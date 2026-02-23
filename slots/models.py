from django.db import models
from locations.models import Temple

class TimeSlot(models.Model):
    temple = models.ForeignKey(Temple, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.PositiveIntegerField()
    booked_count = models.PositiveIntegerField(default=0)

    def is_available(self):
        return self.booked_count < self.capacity

    def __str__(self):
        return f"{self.temple.name} | {self.date} | {self.start_time} - {self.end_time}"