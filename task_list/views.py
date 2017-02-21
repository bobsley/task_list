from django.shortcuts import render, render_to_response
from tasks.models import Task

def index(request):
	return render(request, 'index.html', {'tasks':Task.objects.all()})