from django.shortcuts import render
from django.contrib import messages
from .models import *
import json
# Create your views here.

def indexview(request):
    country=Country.objects.all().order_by('name')
    country_list=list(country.values('name','id'))
    country_list=json.dumps(country_list)

    state=State.objects.all().order_by('name')
    state_list=list(state.values('name','country__name','id'))
    state_list=json.dumps(state_list)

    district=District.objects.all().order_by('name')
    district_list=list(district.values('name','state__name','id'))
    district_list=json.dumps(district_list)

    citie=Citie.objects.all().order_by('name')
    citie_list=list(citie.values('name','district__name','id'))
    citie_list=json.dumps(citie_list)

    messages.success(request,"successfully")

    context={
        "country_list":country_list,
        "state_list":state_list,
        "district_list":district_list,
        "citie_list":citie_list,
    }

    return render(request, 'index.html',context)



from .models import Contact
from .serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
class ContactListCreateAPIView(ListCreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
    lookup_field='id'
