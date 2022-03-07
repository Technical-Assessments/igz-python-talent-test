from urllib import response
from django.test import TestCase
import os
import json
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from django.contrib.auth.models import User
from apps.mathapi.views import matrix_sum_view
from requests.auth import HTTPBasicAuth


USER = os.environ.get('DJANGO_SUPERUSER_USERNAME')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
PASS = os.environ.get('DJANGO_SUPERUSER_PASSWORD')


class MathApiTestCase(TestCase):

    def setUp(self):
        user = User(username=USER, email=EMAIL)
        user.set_password(PASS)
        user.save()


    def test_summ_all_elements_matrix(self):
        client = session()
        endpoint = '/api/matrix/sum/'
        test_data = {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response['Sum of all elements'], 45)


    def test_matrix_type_is_list(self):
        client = session()
        endpoint = '/api/matrix/sum/'
        test_data = {"matrix": "{ [1, 2, 3], [4, 5, 6], [7, 8, 9] }" }
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response["non_field_errors"], ['Input matrix should be a list'])


    def test_matrix_type_not_empty(self):
        client = session()
        endpoint = '/api/matrix/sum/'
        test_data = {"matrix": [] }
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response["non_field_errors"], ['Input matrix is empty'])


    def test_summ_main_diagonal_matrix(self):
        client = session()
        endpoint = '/api/matrix/diagonal_sum/'
        test_data = {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response["Sum of elements in main diagonal"], 15)


    def test_square_matrix(self):
        client = session()
        endpoint = '/api/matrix/diagonal_sum/'
        test_data = {"matrix": [[1, 2], [4, 5, 6], [7, 8, 9]]}
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response["non_field_errors"], ['Input matrix is not square'])


    def test_string_encoder(self):
        client = session()
        endpoint = '/api/string/encode/'
        test_data = {"string": "aaAabaccCBb"}
        request = client.post(endpoint, test_data, format='json')
        response = json.loads(request.content)

        self.assertEqual(response["Encoded string"], "A4B1A1C3B2")


def session():
    client = APIClient()
    client.login(username=USER, password=PASS)

    return client