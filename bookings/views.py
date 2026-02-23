from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import transaction
from .models import Booking, Token
from slots.models import TimeSlot
from .serializers import BookingSerializer

class BookingView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        slot_id = request.data.get('slot_id')
        members = request.data.get('members', 1)

        try:
            with transaction.atomic():
                slot = TimeSlot.objects.select_for_update().get(id=slot_id)

                if slot.booked_count + members > slot.capacity:
                    return Response({'error': 'Slot is full'}, status=status.HTTP_400_BAD_REQUEST)

                booking = Booking.objects.create(
                    user=request.user,
                    slot=slot,
                    members=members
                )

                slot.booked_count += members
                slot.save()

                token = Token.objects.create(booking=booking)

                return Response({
                    'message': 'Booking confirmed',
                    'booking_id': booking.id,
                    'token': str(token.token)
                }, status=status.HTTP_201_CREATED)

        except TimeSlot.DoesNotExist:
            return Response({'error': 'Slot not found'}, status=status.HTTP_404_NOT_FOUND)


class TokenVerificationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token_value = request.data.get('token')

        if not token_value:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = Token.objects.get(token=token_value)

            if token.is_used:
                return Response({'error': 'Token already used'}, status=status.HTTP_400_BAD_REQUEST)

            from django.utils import timezone
            today = timezone.now().date()
            if token.booking.slot.date != today:
                return Response({'error': 'Token not valid for today'}, status=status.HTTP_400_BAD_REQUEST)

            token.is_used = True
            token.save()

            return Response({
                'message': 'Check-in successful',
                'user': token.booking.user.name,
                'temple': token.booking.slot.temple.name,
                'slot': str(token.booking.slot.start_time),
                'members': token.booking.members
            })

        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)