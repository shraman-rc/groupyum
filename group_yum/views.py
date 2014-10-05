#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'groupyum/index.html',{})
def groups(request):
    #return HttpResponse("Hello yo, world. You're at the polls index.")
    return render(request, 'groupyum/test1.html',{})

