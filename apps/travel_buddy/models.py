from django.db import models
from ..login_registration.models import User
from datetime import date
from datetime import datetime

class TripManager(models.Manager):
    def tripValidator(self, postData):
        errors = {}
        today = datetime.now()
        if len(postData['new_city']) < 1 or len(postData['new_state']) < 1 or len(postData['description']) < 1:
            errors['dest-plan'] = 'City, State & Description required.'
        if len(postData['new_date_end']) < 1 or len(postData['new_date_start']) < 1:
            errors['dates'] = 'Please select date for bboth fields.'
            return errors
        from_date = datetime.strptime(postData['new_date_start'],'%Y-%m-%d')
        to_date = datetime.strptime(postData['new_date_end'],'%Y-%m-%d')
        if from_date <= today:
            errors['new_date_start'] = f'Start Date must be after {today})'
            print(postData['new_date_start']) 
        if to_date <= from_date:
            errors['new_date_end'] = f'End Date must be after {from_date}'
        return errors

class Schedule(models.Model):
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    date_start  = models.DateTimeField()
    date_end    = models.DateTimeField()
    plan        = models.CharField(max_length=255)
    creator     = models.ForeignKey(User, related_name='created_trip')
    trip_members= models.ManyToManyField(User, related_name="joined_trips")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = TripManager()
   