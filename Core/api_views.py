from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from datetime import date, timedelta, datetime

class ContactVenue(ReadOnlyModelViewSet):
    queryset = ExitEntryRecord.objects.all()
    serializer_class = VenueSerializer

    def retrieve(self, request, pk, **kwargs):
        diagnosed_date = datetime.strptime(pk, "%Y%m%d")
        visited_venue = Venue.objects.filter(exitentryrecord__date__range = [diagnosed_date-timedelta(days=2),diagnosed_date],\
            exitentryrecord__HKUMember__hkuID=kwargs['member_id'])\
            .order_by('venue_code')\
            .distinct()
        serializer = VenueSerializer(visited_venue, many=True)
        return Response(serializer.data)

class Contactmembers(ReadOnlyModelViewSet):
    queryset = ExitEntryRecord.objects.all()
    serializer_class = ContactSerializer

    def retrieve(self, request, pk, **kwargs):
        close_contact_members = HKUMember.objects.none()
        diagnosed_date = datetime.strptime(pk, "%Y%m%d")
        queryset = ExitEntryRecord.objects\
            .filter(HKUMember__hkuID=kwargs['member_id']) \
            .filter(date__range = [diagnosed_date-timedelta(days=2),diagnosed_date]).values()

        for individual_access in queryset:
            entertime = individual_access['entry_time']
            exittime = individual_access['exit_time']
            accessdate = individual_access['date']
            venueid = individual_access['Venue_id']
            potential_close_contact = ExitEntryRecord.objects\
                .filter(date = accessdate, entry_time__lte = exittime, exit_time__gte = entertime, Venue_id = venueid)\
                .exclude(HKUMember__hkuID=kwargs['member_id']).values()
            for potential_close_contact_access in potential_close_contact:
                close_contact_bool = ((exittime-potential_close_contact_access["entry_time"]>=timedelta(minutes = 30))| (potential_close_contact_access["exit_time"]-entertime>=timedelta(minutes = 30)))
                if(close_contact_bool):
                    close_contact_members = close_contact_members.union(HKUMember.objects.filter(id = potential_close_contact_access['HKUMember_id']))
        close_contact_members = close_contact_members.order_by('hkuID')
        serializer = ContactSerializer(close_contact_members, many=True)
        return Response(serializer.data)