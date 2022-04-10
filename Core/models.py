from django.db import models

# Create your models here.
class TaskForceMember(models.Model):
    username = models.CharField(max_length = 16)
    password = models.CharField(max_length = 16)
    def __str__(self):
        return self.username

class Venue(models.Model):
    venue_code = models.CharField(max_length = 32)
    location = models.CharField(max_length = 256)
    type = models.CharField(max_length = 8)
    capacity = models.IntegerField()
    def __str__(self):
        return self.venue_code

class Device(models.Model):
    username = models.CharField(max_length = 16)
    password = models.CharField(max_length = 16)
    Venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.username} at {self.Venue.venue_code}'

class HKUMember(models.Model):
    hkuID = models.IntegerField()
    name = models.CharField(max_length = 16)
    Venue = models.ManyToManyField(Venue, through='ExitEntryRecord')
    def __str__(self):
        return str(self.hkuID)

class ExitEntryRecord(models.Model):
    date = models.DateField() #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField
    entry_time = models.DateTimeField()  #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateTimeField
    exit_time = models.DateTimeField()
    Venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
    HKUMember = models.ForeignKey(HKUMember, on_delete = models.CASCADE)
    def __str__(self):
        return f'{str(self.HKUMember.hkuID)} entered {self.Venue.venue_code} at {self.entry_time} and exited at {self.exit_time}'