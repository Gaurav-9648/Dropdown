from django.db import models
from myapp.models import Country, State, District, Citie
from django.contrib.auth.models import User
class Location(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='location')
    phone=models.CharField(max_length=100,blank=True, null= True)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, related_name='cntry')
    state=models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True, related_name='dvsn')
    district=models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, related_name='dstrct')
    citie=models.ForeignKey(Citie, on_delete=models.SET_NULL, blank=True, null=True, related_name='sbdstrct')
    