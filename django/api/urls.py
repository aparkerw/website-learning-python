from django.urls import path
from .views import RecordView

from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('echo', views.echo, name='echo'),
    path('records', RecordView.as_view()),
]