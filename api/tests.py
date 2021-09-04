from django.urls import include, path
from api.models import Invoice, Transactions
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient, URLPatternsTestCase


class InvoiceTest(APITestCase):

    def test_post(self):
        url = 'http://127.0.0.1:8000/invoice/'
        data = {
            "customer": "v1",
            "date": "2021-09-05",
            "transactions": [{
                              "product": "p1",
                              "quantity": 12,
                              "price": "33.00"

                              },
                             {
                                 "product": "p2",
                                 "quantity": 3,
                                 "price": "33.00"
                             }
                             ]

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put(self):
        url = 'http://127.0.0.1:8000/invoice/1/'
        data = {
            "id": 1,
            "customer": "v1",
            "date": "2021-09-05",
            "transactions": [{
                "product": "p1",
                "quantity": 12,
                "price": "33.00"

            },
                {
                    "product": "p2",
                    "quantity": 3,
                    "price": "33.00"
                }
            ]

        }
        Invoice.objects.create(id=1, customer='v1').save()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_del(self):
        url = 'http://127.0.0.1:8000/invoice/1/'
        Invoice.objects.create(id=1, customer='v1').save()
        response = self.client.delete(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

