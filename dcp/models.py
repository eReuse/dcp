from django.db import models
from django.contrib.gis.db import models as gis_models


class Place(models.Model):
    # enum values for OrganizationalStructure
    RECYCLING_POINT = 'RecyclingPoint'
    TYPES = (
        (RECYCLING_POINT, 'Recycling Point'),
    )
    
    label = models.CharField(max_length=256, unique=True,
                             help_text='Human friendly name of the Place')
    sameAs = models.URLField(help_text='URL identifying the organization in '
                                       'the IT Device Manager which possess '
                                       'it.',
                             blank=True)
    geo = gis_models.PolygonField()  # TODO how to store a circle
    type = models.CharField(max_length=16, choices=TYPES, default=RECYCLING_POINT)
    
    objects = gis_models.GeoManager()
    
    def __str__(self):
        return "{0} ({1})".format(self.label, self.type)
