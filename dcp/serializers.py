from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source='sameAs')
    
    class Meta:
        model = Place
        fields = ('label', 'url', 'type', 'geo')
