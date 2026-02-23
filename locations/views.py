from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Temple
from .serializers import TempleSerializer

class TempleListView(APIView):
    def get(self, request):
        city = request.query_params.get('city', None)
        if city:
            temples = Temple.objects.filter(city__icontains=city, is_active=True)
        else:
            temples = Temple.objects.filter(is_active=True)
        serializer = TempleSerializer(temples, many=True)
        return Response(serializer.data)