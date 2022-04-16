from django.db import router
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'ExitEntry/(?P<hkuID>[^/.]+)/(?P<venue_code>[^/]+)/(?P<date>[^/]+)', ExitEntryViewSet)
router.register(r'members', hkuMembersViewSet)
router.register(r'venues', VenuesViewset)

#e.g. http://127.0.0.1:8000/Core/members/close-contacts/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/venues/infectious-venues/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/ExitEntry/3030012345/CPD-LG.02/20220106-09:15:32/
#All use GET method
#for Core/exitentry/... : Returns 'Entry...' or 'Exit...' 

urlpatterns = [
    path('venues/infectious-venues/<str:hkuID>/<str:date>/', ContactVenue),
    path('members/close-contacts/<str:hkuID>/<str:date>/', ContactMember),
    path('', include(router.urls)),
]

