from django.urls import path
import api.views
urlpatterns = [
    path('', api.views.index),
]