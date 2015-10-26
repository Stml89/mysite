__author__ = 'stml'
from django.shortcuts import render_to_response
from django.http import HttpResponse

def hello(request):
    return render_to_response('pages/index.html')