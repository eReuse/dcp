from django.contrib.gis.geos import Point
from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import ParseError


class GeoPointFilterBackend(BaseFilterBackend):
    lat_param = 'lat'
    lng_param = 'lng'
    
    def get_filter_point(self, request):
        lat_string = request.query_params.get(self.lat_param, None)
        lng_string = request.query_params.get(self.lng_param, None)
        
        if not lat_string or not lng_string:
            return None
        
        try:
            x = float(lat_string)
        except ValueError:
            raise ParseError('Invalid geometry string supplied for parameter '
                             '{0}'.format(self.lat_param))
        try:
            y = float(lng_string)
        except ValueError:
            raise ParseError('Invalid geometry string supplied for parameter '
                             '{0}'.format(self.lng_param))
        
        return Point(x, y)
    
    def filter_queryset(self, request, queryset, view):
        point = self.get_filter_point(request)
        
        if not point:
            return queryset
        
        point = self.get_filter_point(request)
        return queryset.filter(geo__contains=point)
