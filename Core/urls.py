from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'contacts/(?P<member_id>[^/.]+)', ContactMembers)
router.register(r'venues/(?P<member_id>[^/.]+)', ContactVenue)
router.register(r'exitentry/(?P<member_id>[^/.]+)/(?P<venue_name>[^/]+)', UpdateExitEntry)

#e.g. http://127.0.0.1:8000/Core/contacts/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/venues/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/exitentry/3030012345/CPD-LG.02/20220105-09:15:32/
#All use GET method
#for Core/exitentry/... : Returns 'Entered' or 'Exited' 

urlpatterns = [
    path('', include(router.urls)),
]

