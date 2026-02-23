import uuid
from django.db import models
from users.models import User
from slots.models import TimeSlot

class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='bookings')
    members = models.PositiveIntegerField(default=1)  # number of visitors
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} | {self.slot} | {self.status}"


class Token(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='token')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)