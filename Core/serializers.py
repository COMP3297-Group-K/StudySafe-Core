from rest_framework import serializers
from .models import *

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = HKUMember
        fields = ['hkuID','name']

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ['venue_code']