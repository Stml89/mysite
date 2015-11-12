__author__ = 'stml'
from django.shortcuts import render_to_response
# from django.http import HttpResponse
# from django.template.loader import get_template
import datetime

# def Error_404(request):
#     return render_to_response('index.html', {'Error_404': 'true'})

def main_page(request):
    return render_to_response('index.html', {'home_page': 'true'})

def service_page(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'service_page': 'true'})

def contact_page(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'contact': 'true'})

def electrical_page(request):
    now = datetime.datetime.now()
    return render_to_response('index.html', {'electrical_page': 'true'})