from django.urls import path
from mi.views import *

app_name='hari'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]
