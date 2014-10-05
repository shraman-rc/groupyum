from django.http import HttpResponse
from django.shortcuts import render

def groups(request):
    return render(request, 'groups.html', {})

def signup(request):
    return render(request, 'signup.html', {})