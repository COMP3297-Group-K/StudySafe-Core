from django.db import router
from django.urls import path, include
from Core import views
from rest_framework.routers import DefaultRouter
from .api_views import *

router = DefaultRouter()
router.register(r'contacts/(?P<member_id>[^/.]+)', Contactmembers)
router.register(r'venues/(?P<member_id>[^/.]+)', ContactVenue)

#e.g. http://127.0.0.1:8000/Core/contacts/3030012345/20220411/
#e.g. http://127.0.0.1:8000/Core/venues/3030012345/20220411/

urlpatterns = [
    path('', include(router.urls)),
]

