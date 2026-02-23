from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TimeSlot
from .serializers import TimeSlotSerializer

class SlotListView(APIView):
    def get(self, request):
        temple_id = request.query_params.get('temple_id')
        date = request.query_params.get('date')

        if not temple_id or not date:
            return Response({'error': 'temple_id and date are required'}, status=status.HTTP_400_BAD_REQUEST)

        slots = TimeSlot.objects.filter(temple_id=temple_id, date=date)
        serializer = TimeSlotSerializer(slots, many=True)
        return Response(serializer.data)