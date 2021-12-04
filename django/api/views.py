from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RecordSerializer
from .models import Record
import datetime

# Create your views here.
def main(request):
    return HttpResponse('hello')

def echo(request):
    now = datetime.datetime.now()
    html = "<html><body>Echo: %s.</body></html>" % now
    return HttpResponse(html)

class RecordView(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    