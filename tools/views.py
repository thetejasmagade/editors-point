from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

# Create your views here.
def punctuationremover(request):
    return render(request, 'tools/punctuationremover.html')
