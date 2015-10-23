from django.contrib.auth import get_user_model
# TODO decouple from grd
#from rest_framework.test import APILiveServerTestCase
from grd.functional_tests.common import BaseTestCase

from dcp.models import Place


User = get_user_model()


#class FilterPointTest(APILiveServerTestCase):
class FilterPointTest(BaseTestCase):
    fixtures = ['places.json']
    
#    def setUp(self):
#        super(FilterPointTest, self).setUp()
#        token = self.get_user_token('ereuse', 'ereuse')
#        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    
    def test_retrieve_place_list(self):
        response = self.client.get('/api/places/')
        self.assertEqual(200, response.status_code)
    
    def test_filter_invalid_lat(self):
        response = self.client.get('/api/places/?lat=1&lng=INVALID')
        self.assertEqual(400, response.status_code)

    def test_filter_invalid_lng(self):
        response = self.client.get('/api/places/?lat=INVALID&lng=0.2')
        self.assertEqual(400, response.status_code)
    def test_filter_no_results(self):
        response = self.client.get('/api/places/?lat=1&lng=100')
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.data['count'])
        
    def test_filter_single_result(self):
        response = self.client.get('/api/places/?lat=1&lng=0.5')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.data['count'])
    
    # TODO could have several results??
    # That will mean that there are overlaped places?
