from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
#import requests


def index(request):
	return render(request, 'WRMLandingPage.html')