from django.urls import path
from app2.views import *
app_name='something2'
urlpatterns=[
    path('first/',first,name='first.html'), 
    path('second/',second,name='second.html'),
]