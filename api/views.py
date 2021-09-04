from django.shortcuts import HttpResponse


def index(req):
    return HttpResponse("It's Working!")

# Create your views here.
