from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mouni(request):
    return HttpResponse('<marquee><h1>mounika reddy daughter of raja reddy</h1></marquee>')

def chandu(request):
    return HttpResponse('om prakash reddy')