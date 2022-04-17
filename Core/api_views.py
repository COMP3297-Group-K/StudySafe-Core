from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view
from django.db.models import F
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import mixins
from datetime import date, timedelta, datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

# adding parameters documentation
test_param = [
    openapi.Parameter('hkuID', openapi.IN_PATH, description="HKU ID of the infected member", type=openapi.TYPE_STRING),
    openapi.Parameter('date', openapi.IN_PATH, description="Infection date of the corresponding member", type=openapi.TYPE_STRING),
]
user_response = openapi.Response('A list of venues visted by the input member', VenueSerializer)

@swagger_auto_schema(
    method='get', operation_description="List all venues visited by HKU members with id `hkuID`, infected time `date`",\
    manual_parameters=test_param, responses={200: user_response})
@api_view(['GET',])
def ContactVenue(request, hkuID: int, date: int): #https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
    """list all venues visited by HKU members with id `hkuID`, infected time `date`

    Args:
        hkuID (int): HKU id of the infected people
        date (int): infection time
    """
    diagnosed_date = datetime.strptime(str(date), "%Y%m%d")
    visited_venue = Venue.objects.filter(exitentryrecord__date__range = [diagnosed_date-timedelta(days=2),diagnosed_date],\
            exitentryrecord__HKUMember__hkuID=hkuID)\
            .order_by('venue_code')\
            .distinct()
    serializer = VenueSerializer(visited_venue, many=True)
    return Response(serializer.data)

user_response = openapi.Response('A list of close contacts of the input infected member', MemberSerializer)
@swagger_auto_schema(
    method='get', operation_description="List the close contacts of HKU members with id `member_id`, infected time `date`",\
    manual_parameters=test_param, responses={200: user_response})
@api_view(['GET',])
def ContactMember(request, hkuID, date):
    close_contact_members = HKUMember.objects.none()
    diagnosed_date = datetime.strptime(str(date), "%Y%m%d")
    queryset = ExitEntryRecord.objects\
        .filter(HKUMember__hkuID=hkuID) \
        .filter(date__range = [diagnosed_date-timedelta(days=2),diagnosed_date]).values()

    for individual_access in queryset:
        entertime = individual_access['entry_time']
        exittime = individual_access['exit_time']
        accessdate = individual_access['date']
        venueid = individual_access['Venue_id']
        potential_close_contact = ExitEntryRecord.objects\
            .filter(date = accessdate, entry_time__lte = exittime, exit_time__gte = entertime, Venue_id = venueid)\
            .exclude(HKUMember__hkuID=hkuID).values()
        for potential_close_contact_access in potential_close_contact:
            close_contact_bool = ((exittime-potential_close_contact_access["entry_time"]>=timedelta(minutes = 30))| (potential_close_contact_access["exit_time"]-entertime>=timedelta(minutes = 30)))
            if(close_contact_bool):
                close_contact_members = close_contact_members.union(HKUMember.objects.filter(hkuID = potential_close_contact_access['HKUMember_id']))
    close_contact_members = close_contact_members.order_by('hkuID')
    serializer = MemberSerializer(close_contact_members, many=True)
    return Response(serializer.data)


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
    serializer_class = ExitEntryRecordSerializer

    @swagger_auto_schema(
        operation_description="Create the exit or entry record of member `hkuID` at venue `venue_code`")
    def create(self, request):

        data = request.POST
        time = datetime.strptime(data['date'],"%Y%m%d-%H:%M:%S")
        date = time.date()
        member_id = data['hkuID']
        venue_name = data['venue_code']
        obj = ExitEntryRecord.objects.filter(HKUMember__hkuID = member_id, date = date, exit_time = F('entry_time'))
        if obj:
            obj.exit_time = time
            obj.save()
        else:
            created = ExitEntryRecord(date=date, HKUMember=HKUMember.objects.get(hkuID = member_id), entry_time=time, exit_time=time, Venue=Venue.objects.get(venue_code = venue_name))
    # def create(self, request, **kwargs):

    #     time = datetime.strptime(kwargs['date'],"%Y%m%d-%H:%M:%S")
    #     date = time.date()
    #     member_id = kwargs['hkuID']
    #     venue_name = kwargs['venue_code']
    #     obj = ExitEntryRecord.objects.filter(HKUMember__hkuID = member_id, date = date, exit_time = F('entry_time'))
    #     if obj:
    #         obj.exit_time = time
    #         obj.save()
    #     else:
    #         created = ExitEntryRecord(date=date, HKUMember=HKUMember.objects.get(hkuID = member_id), entry_time=time, exit_time=time, Venue=Venue.objects.get(venue_code = venue_name))

    @swagger_auto_schema(
        operation_description="Retrive the exit or entry record of member `hkuID` at venue `venue_code`",\
        responses={200: openapi.Response('The exit or entry record of the input member', ExitEntryRecordSerializer)})
    def list(self, request, *args, **kwargs):
        time = datetime.strptime(kwargs['date'],"%Y%m%d-%H:%M:%S")
        date = time.date()
        member_id = kwargs['hkuID']
        venue_name = kwargs['venue_code']
        obj = ExitEntryRecord.objects.filter(HKUMember__hkuID = member_id, date=date, Venue=venue_name)
        serializer = ExitEntryRecordSerializer(obj, many=True)
        return Response(serializer.data)

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
