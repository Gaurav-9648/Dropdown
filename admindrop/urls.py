from django.urls import path
from .views import *
urlpatterns = [
    path('states/',StateList.as_view()),
    path('districts/',DistrictList.as_view()),
    path('cities/',CitieList.as_view()),
]
