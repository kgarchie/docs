from unicodedata import name

import django
from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('doc/<int:id>', views.doc, name='doc'),
]