from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class State(models.Model):
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country,on_delete=models.CASCADE, related_name='states')
    def __str__(self):
        return self.name
class District(models.Model):
    name=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE, related_name='districts')
    def __str__(self):
        return self.name
class Citie(models.Model):
    name=models.CharField(max_length=100)
    district=models.ForeignKey(District,on_delete=models.CASCADE, related_name='cities')
    def __str__(self):
        return self.name

class Address(models.Model):
    addressOf=models.CharField(max_length=100)
    country=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='country_set')
    state=models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='state_set')
    district=models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True, related_name='district_set')
    citie=models.ForeignKey(Citie, on_delete=models.SET_NULL, null=True, blank=True, related_name='citie_set')
    def __str__(self):
        return self.addressOf




class Contact(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    email=models.EmailField()
    text=models.TextField()
    def __str__(self):
        return self.name