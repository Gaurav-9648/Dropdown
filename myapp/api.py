from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.http import JsonResponse
class StateListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        country = request.data['country']
        state = {}
        if country:
            states = Country.objects.get(id=country).states.all()
            state = {pp.name:pp.id for pp in states}
        return JsonResponse(data=state, safe=False)
class DistrictListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        state = request.data['state']
        district = {}
        if state:
            districts = State.objects.get(id=state).districts.all()
            district = {pp.name:pp.id for pp in districts}
        return JsonResponse(data=district, safe=False)
class CitieListAPIView(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        state = request.data['district']
        district = {}
        if state:
            districts = District.objects.get(id=district).cities.all()
            district = {pp.name:pp.id for pp in districts}
        return JsonResponse(data=district, safe=False)
