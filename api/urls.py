from django.urls import path, include
from rest_framework import routers

import api.views

router = routers.DefaultRouter()
router.register(r'invoice', api.views.InvoiceViewSet)
urlpatterns = [
    path('', api.views.index),
    path('', include(router.urls)),
]
