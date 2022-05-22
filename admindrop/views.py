from django.http.response import JsonResponse
from myapp.models import Country, District, State
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class StateList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        country=request.data['country']
        division={}
        if country:
            states=Country.objects.get(id=country).states.all()
            state={p.name:p.id for p in states}
        return JsonResponse(data=state, safe=False)
class DistrictList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        state=request.data['state']
        district={}
        if state:
            districts=State.objects.get(id=state).districts.all()
            district={p.name:p.id for p in districts}
        return JsonResponse(data=district, safe=False)
class CitieList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        district=request.data['district']
        citie={}
        if district:
            cities=District.objects.get(id=district).cities.all()
            citie={p.name:p.id for p in cities}
        return JsonResponse(data=citie, safe=False)
