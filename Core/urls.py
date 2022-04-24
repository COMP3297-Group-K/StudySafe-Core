from django.db import router
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'ExitEntry', ExitEntryViewSet)
router.register(r'members', hkuMembersViewSet)
router.register(r'venues', VenuesViewset)

#e.g. http://127.0.0.1:8000/Core/members/close-contacts/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/venues/infectious-venues/3030012345/20220411/

urlpatterns = [
    path('venues/infectious-venues/<str:hkuID>/<str:date>/', ContactVenue),
    path('members/close-contacts/<str:hkuID>/<str:date>/', ContactMember),
    path('', include(router.urls)),
]

