from django.db import router
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'ExitEntry/(?P<member_id>[^/.]+)/(?P<venue_name>[^/]+)', ExitEntryViewSet)
router.register(r'members', hkuMembersViewSet)
router.register(r'venues', VenuesViewset)

#e.g. http://127.0.0.1:8000/Core/ContactMember/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/ContactVenue/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220106-09:15:32/
#All use GET method
#for Core/exitentry/... : Returns 'Entry...' or 'Exit...' 

urlpatterns = [
    path('venues/infectious-venues/<int:member_id>/<int:date>/', ContactVenue),
    path('members/close-contacts/<int:member_id>/<int:date>/', ContactMember),
    path('', include(router.urls)),
]

