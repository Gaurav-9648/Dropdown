
from django.contrib import admin
from django.urls import path,include
from myapp.views import *
from myapp.api import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexview),
    path('contact/',ContactListCreateAPIView.as_view()),
    path('states/',  StateListAPIView.as_view()),
    path('districts/',  DistrictListAPIView.as_view()),
    path('cities/', CitieListAPIView.as_view()),
    path('admindrop/',include('admindrop.urls')),
    path('contact/<int:id>/',ContactRetrieveUpdateDestroyAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
