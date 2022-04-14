from django.db import router
from django.urls import path, include
from Trace import views

urlpatterns = [
    path('venues', views.ViewVenuesAll.as_view()),
    path('contacts', views.ViewContactsAll.as_view()),
    path('venues/<int:hkuID>', views.ViewVenues.as_view(), name='venues-members'),
    path('contacts/<int:hkuID>', views.ViewContacts.as_view(), name='contacts-members'),
]