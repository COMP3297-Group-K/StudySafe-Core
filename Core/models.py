from django.db import models

# Create your models here.

# class TaskForceMember(models.Model):
#     username = models.CharField(max_length = 16)
#     password = models.CharField(max_length = 16)
#     first_name = models.CharField(max_length = 32)
#     last_name = models.CharField(max_length = 32)
#     email = models.CharField(max_length = 32)
#     def __str__(self):
#         return self.username

# class Device(models.Model):
#     username = models.CharField(max_length = 16)
#     password = models.CharField(max_length = 16)
#     Venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
#     def __str__(self):
#         return f'{self.username} at {self.Venue.venue_code}'

class Venue(models.Model):
    venue_code = models.CharField(max_length = 20, primary_key = True)
    location = models.CharField(max_length = 150)
    type = models.CharField(max_length = 8)
    capacity = models.IntegerField()
    def __str__(self):
        return self.venue_code

class HKUMember(models.Model):
    hkuID = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length = 150)
    Venue = models.ManyToManyField(Venue, through='ExitEntryRecord')
    def __str__(self):
        return f'{self.hkuID} {self.name}'

class ExitEntryRecord(models.Model):
    date = models.DateField() #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateField
    entry_time = models.DateTimeField()  #https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.DateTimeField
    exit_time = models.DateTimeField()
    Venue = models.ForeignKey(Venue, on_delete = models.CASCADE)
    HKUMember = models.ForeignKey(HKUMember, on_delete = models.CASCADE)
    def __str__(self):
        return f'{str(self.HKUMember.hkuID)} entered {self.Venue.venue_code} at {self.entry_time} and exited at {self.exit_time}'