from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('mouni/',mouni,name='mouni'),
    path('chandu/',chandu,name='chandu'),
]