from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'places', views.PlaceView)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
