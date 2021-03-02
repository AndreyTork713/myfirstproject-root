from django.http import HttpResponse
from django.shortcuts import render


def about(request):
	return HttpResponse('This is about page...')


def home(request):
	return render(request, 'home.html', {'greeting': 'Hello!'})

def gogo(request):
	return render(request, 'gogo.html', {'g1': 'This is first G!',
		'o1': 'This is first O!', 'g2': 'This is second G!', 'o2':
		'This is second O!'})