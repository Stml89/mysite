__author__ = 'stml'
from django.shortcuts import render_to_response
# from django.http import HttpResponse

# def Error_404(request):
#     return render_to_response('index.html', {'Error_404': 'true'})

def main_page(request):
    return render_to_response('index.html', {'home_page': 'true'})