from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import api_view
from django.db.models import F
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from datetime import date, timedelta, datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

# adding parameters documentation
test_param = [
    openapi.Parameter('member_id', openapi.IN_PATH, description="HKU ID of the infected member", type=openapi.TYPE_STRING),
    openapi.Parameter('date', openapi.IN_PATH, description="Infection date of the corresponding member", type=openapi.TYPE_STRING),
]
user_response = openapi.Response('A list of venues visted by the input member', VenueSerializer)

@swagger_auto_schema(
    method='get', operation_description="List all venues visited by HKU members with id `member_id`, infected time `date`",\
    manual_parameters=test_param, responses={200: user_response})
@api_view(['GET',])
def ContactVenue(request, member_id: int, date: int): #https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
    """list all venues visited by HKU members with id `member_id`, infected time `date`

    Args:
        member_id (int): HKU id of the infected people
        date (int): infection time
    """
    diagnosed_date = datetime.strptime(str(date), "%Y%m%d")
    visited_venue = Venue.objects.filter(exitentryrecord__date__range = [diagnosed_date-timedelta(days=2),diagnosed_date],\
            exitentryrecord__HKUMember__hkuID=member_id)\
            .order_by('venue_code')\
            .distinct()
    serializer = VenueSerializer(visited_venue, many=True)
    return Response(serializer.data)

user_response = openapi.Response('A list of close contacts of the input infected member', MemberSerializer)
@swagger_auto_schema(
    method='get', operation_description="List the close contacts of HKU members with id `member_id`, infected time `date`",\
    manual_parameters=test_param, responses={200: user_response})
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

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="List all entry exit records"))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Create an entry exit record"))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="List entry exit record with `id`"))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Modify entry exit record with `id`"))  
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="Modify entry exit record with `id`"))  
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Delete entry exit record with `id`"))    
class ExitEntryViewSet(ModelViewSet):
    queryset = ExitEntryRecord.objects.all()

    @swagger_auto_schema(
        operation_description="Retrieve the exit or entry record of member `member_id` at venue `venue_name`",\
        responses={200: openapi.Response('Text field specifying exit or entry', type=openapi.TYPE_STRING)})
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

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="List all HKU members"))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Create a HKU member"))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="List HKU member with `hkuID`"))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Modify HKU member with `hkuID`"))  
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="Modify HKU member with `hkuID`"))  
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Delete HKU member with `hkuID`"))      
class hkuMembersViewSet(ModelViewSet):
    queryset = HKUMember.objects.all()
    serializer_class = MemberSerializer

@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_description="List all venues"))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description="Create a venue"))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_description="List venue with `venue_code`"))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_description="Modify venue with `venue_code`"))  
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description="Modify venue with `venue_code`"))  
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_description="Delete venue with `venue_code`"))     
class VenuesViewset(ModelViewSet):
    lookup_value_regex = '[\d\w\-\.]+'
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
