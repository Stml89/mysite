__author__ = 'stml'
from django.shortcuts import render_to_response
# from django.http import HttpResponse
# from django.template.loader import get_template
import datetime

def main_page(request):
    return render_to_response('index.html', {'home_page': 'true'})

def service_page(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'service_page': 'true'})

def contact_page(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'contact_page': 'true'})

def electrical_work(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'electrical_work': 'true'})