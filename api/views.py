from django.shortcuts import HttpResponse
from rest_framework.viewsets import ModelViewSet

import api.serializers
from api.models import Invoice


def index(req):
    return HttpResponse("It's Working!")


class InvoiceViewSet(ModelViewSet):
    serializer_class = api.serializers.InvoiceSerializer
    queryset = Invoice.objects.all()
