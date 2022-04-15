from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import api_view
from django.db.models import F
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from datetime import date, timedelta, datetime

@api_view(['GET',])
def ContactVenue(request, member_id, date): #https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
    diagnosed_date = datetime.strptime(str(date), "%Y%m%d")
    visited_venue = Venue.objects.filter(exitentryrecord__date__range = [diagnosed_date-timedelta(days=2),diagnosed_date],\
            exitentryrecord__HKUMember__hkuID=member_id)\
            .order_by('venue_code')\
            .distinct()
    serializer = VenueSerializer(visited_venue, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def ContactMember(request, member_id, date):
    close_contact_members = HKUMember.objects.none()
    diagnosed_date = datetime.strptime(str(date), "%Y%m%d")
    queryset = ExitEntryRecord.objects\
        .filter(HKUMember__hkuID=member_id) \
        .filter(date__range = [diagnosed_date-timedelta(days=2),diagnosed_date]).values()

    for individual_access in queryset:
        entertime = individual_access['entry_time']
        exittime = individual_access['exit_time']
        accessdate = individual_access['date']
        venueid = individual_access['Venue_id']
        potential_close_contact = ExitEntryRecord.objects\
            .filter(date = accessdate, entry_time__lte = exittime, exit_time__gte = entertime, Venue_id = venueid)\
            .exclude(HKUMember__hkuID=member_id).values()
        for potential_close_contact_access in potential_close_contact:
            close_contact_bool = ((exittime-potential_close_contact_access["entry_time"]>=timedelta(minutes = 30))| (potential_close_contact_access["exit_time"]-entertime>=timedelta(minutes = 30)))
            if(close_contact_bool):
                close_contact_members = close_contact_members.union(HKUMember.objects.filter(hkuID = potential_close_contact_access['HKUMember_id']))
    close_contact_members = close_contact_members.order_by('hkuID')
    serializer = MemberSerializer(close_contact_members, many=True)
    return Response(serializer.data)

class ExitEntryViewSet(ModelViewSet):
    queryset = ExitEntryRecord.objects.all()

    def retrieve(self, request, pk, **kwargs):
        time = datetime.strptime(pk,"%Y%m%d-%H:%M:%S")
        date = time.date()
        member_id = kwargs['member_id']
        venue_name = kwargs['venue_name']
        obj, created = ExitEntryRecord.objects.get_or_create(HKUMember__hkuID = member_id, date = date, exit_time = F('entry_time'),
        defaults={'entry_time': time, 'exit_time': time,
            'Venue': Venue.objects.get(venue_code = venue_name),
            'HKUMember': HKUMember.objects.get(hkuID = member_id) }
        )
        if created:
            return HttpResponse("Entry record was recorded.")
        else:
            obj.exit_time = time
            obj.save()
            return HttpResponse("Exit record was recored.")

        
class hkuMembersViewSet(ModelViewSet):
    queryset = HKUMember.objects.all()
    serializer_class = MemberSerializer

class VenuesViewset(ModelViewSet):
    lookup_value_regex = '[\d\w\-\.]+'
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
