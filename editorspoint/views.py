from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')