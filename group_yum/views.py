from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from models import User

def index(request):
    return render(request, 'index.html', {})

def groups(request):
    return render(request, 'groups.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def createUser(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']

    stripWords = ["dorm","house","fraternity","frat","sorority"]
    abbreviations = {"EC":"east campus", "BC":"burton conner"}
    living_group = request.POST['living_group'].lower().replace('-',' ')
    living_group = ' '.join([word for word in living_group.split() if word not in stripWords])
    living_group = ' '.join([abbreviations[abbr] for abbr in living_group.split() if abbr in abbreviations])
    
    newUser = User(first_name=first_name, last_name=last_name, email=email, password=password, date_joined=timezone.now())
    newUser.save()

    # SHOULD REDIRECT TO LOGIN PAGE
    return redirect("index")
