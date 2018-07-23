from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import IntegrityError ##Exception raised when the relational integrity of the database is affected, e.g. a foreign key check fails, duplicate key, etc.
import bcrypt
from .models import *

def logged_in(request):
    if 'id' in request.session:
        context = {
            'user_schedules': Schedule.objects.filter(creator=request.session['id']),
            'joined_schedules': User.objects.get(id=request.session['id']).joined_trips.all(),
            # 'user_schedules': Schedule.objects.filter(trip_members=request.session['id']),
            'all_schedules': Schedule.objects.exclude(creator=request.session['id']).exclude(trip_members=request.session['id'])
        }
        return render(request,'travel_buddy/index.html', context)
    else:
        return redirect('/')

def new(request):
    return render(request, 'travel_buddy/new.html')

def create(request):
    print(request.POST, "-----------")
    errors = Schedule.objects.tripValidator(request.POST)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        return redirect('/travel_buddy/new')
    user = User.objects.get(id=request.session['id'])
    Schedule.objects.create(city = request.POST['new_city'], state = request.POST['new_state'], date_start = request.POST['new_date_start'], date_end = request.POST['new_date_end'], plan = request.POST['description'], creator = user)
    return redirect('/travel_buddy')

def destroy(request,id):
    Schedule.objects.get(id=id).delete()
    return redirect('/travel_buddy')

def show(request, id):
    trip = Schedule.objects.get(id=id)
    context = { 
        'schedule': Schedule.objects.get(id=id),
        'user': User.objects.get(id=request.session['id']),
        'all_users': trip.trip_members.all()
    }
    return render(request,'travel_buddy/show.html', context)

def join(request,id):
    user = User.objects.get(id=request.session['id'])
    schedule = Schedule.objects.get(id=id)
    user.joined_trips.add(schedule)
    return redirect('/travel_buddy')

def cancel(request, id):
    user = User.objects.get(id=request.session['id'])
    schedule = Schedule.objects.get(id=id)
    user.joined_trips.remove(schedule)
    return redirect('/travel_buddy')

def logout(request):
    request.session.flush()
    return redirect('/')
