from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError ##Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
import bcrypt
from .models import User

def index(request):
    return render(request,'login_registration/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        try:
            User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],username = request.POST['username'],password = pwHash)
        except IntegrityError: #Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
            messages.error(request, 'this username already exists', extra_tags='username')
            return redirect('/')
    request.session['first_name'] = request.POST['first_name']
    return redirect('/travel_buddy')   

def login(request):
    try:
        user = User.objects.get(username=request.POST['login_username'])
        if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            request.session['first_name'] = user.first_name
            request.session['id'] = user.id
            return redirect('/travel_buddy')
    except User.DoesNotExist: #https://stackoverflow.com/questions/14255125/catching-doesnotexist-exception-in-a-custom-manager-in-django 
        pass
    messages.error(request, 'Please check username/passowrd, and try again.', extra_tags='login')
    return redirect('/')

