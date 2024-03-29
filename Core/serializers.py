from pyexpat import model
from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = HKUMember
        fields = ['hkuID','name']

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = '__all__'

class ExitEntryRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExitEntryRecord
        fields = '__all__'