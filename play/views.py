from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "play/index.html")
