from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer

# Create your views here.

class ListSongsView(generics.ListAPIView):
    """
    Provide a get method handler
    """
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
