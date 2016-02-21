from django.contrib.gis import admin

from .models import Place


class PlaceAdmin(admin.OSMGeoAdmin):
    # coordinates on SRID=900913
    # https://code.djangoproject.com/ticket/11094
    default_lon = 236037
    default_lat = 5068987
    default_zoom = 7
    map_height = 500
    map_width = 800


admin.site.register(Place, PlaceAdmin)
