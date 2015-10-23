from django.db import models
from django.contrib.gis.db import models as gis_models


class Place(models.Model):
    TYPES = ()  # TODO set enum values for OrganizationalStructure
    
    label = models.CharField(max_length=256, unique=True,
                             help_text='Human friendly name of the Place')
    sameAs = models.URLField(help_text='URL identifying the organization in '
                                       'the IT Device Manager which possess '
                                       'it.')
    geo = gis_models.PolygonField()  # TODO how to store a circle
    type = models.CharField(max_length=16)#, choices=TYPES)
    
    objects = gis_models.GeoManager()
