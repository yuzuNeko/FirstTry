from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse('nihao')
def show(request):

	return render(request,'show.html')