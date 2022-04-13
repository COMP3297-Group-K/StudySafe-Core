from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json

# Create your views here.

class View(TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'venues/'
        self.data = []
        self.subject = 0
        self.date = 00000000
    
    def get_infected(self):
        with open('json_data.json') as json_file:
            self.infected = (json.load(json_file))

    def get_data(self):
        # self.data = []
        for infected in self.infected['infected']:
            hkuID, date = infected['hkuID'], infected['date']
            path = 'http://localhost:8000/Core/' + self.head + str(hkuID) + '/' + str(date)
            try:
                data = requests.get(url=path)
            except:
                self.error = 1
            else: 
                self.data += json.loads(data.text)
        self.unique()

    def unique(self):
        res = []
        for data in self.data:
            if data not in res:
                res.append(data)
        self.data = res
    
    def get_context_data(self, **kwargs):
        self.get_infected()
        self.get_data()
        context = dict()
        context['error'] = self.error
        context['data'] = self.data
        context['subject'] = self.subject
        context['date'] = self.date
        return context


class ViewVenuesAll(View):
    template_name = "venues.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'venues/'
        self.data = []
        self.subject = 0
        self.date = 00000000


class ViewContactsAll(View):
    template_name = "contacts.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'contacts/'
        self.data = []
        self.subject = 0
        self.date = 00000000

class ViewVenues(View):
    template_name = "venues.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'venues/'
        self.data = []
        self.subject = 0
        self.date = 00000000

    def get_infected(self, **kwargs):
        with open('json_data.json') as json_file:
            infected = (json.load(json_file))
        hkuID = self.kwargs['hkuID']
        flag = 0
        for member in infected['infected']:
            if member['hkuID'] == hkuID:
                self.infected = {'infected': [{'hkuID': member['hkuID'], 'date': member['date']}]}
                self.subject, self.date = member['hkuID'], member['date']
                flag = 1
        self.error = (flag == 0)

class ViewContacts(ViewVenues):
    template_name = "contacts.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'contacts/'
        self.data = []
        self.subject = 0
        self.date = 00000000

if __name__ == '__main__':
    venues = ViewVenues()
    print(venues.get_context_data())
    contacts = ViewContacts()
    print(contacts.get_context_data())
    print(contacts.data)