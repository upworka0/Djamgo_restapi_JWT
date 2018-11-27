from .models import Songs
from rest_framework import serializers

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'artist')
