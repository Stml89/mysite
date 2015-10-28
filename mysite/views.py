__author__ = 'stml'
from django.shortcuts import render_to_response
from django.http import HttpResponse
# from django.template.loader import get_template
import datetime

def hello(request):
    return render_to_response('index.html')

def hello2(request):
    now = datetime.datetime.now()
    return render_to_response('second.html', {'current_date': now})