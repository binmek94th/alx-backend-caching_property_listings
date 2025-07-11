from django.urls import path
from rest_framework.routers import DefaultRouter

from properties.views import property_list

router = DefaultRouter()


urlpatterns = [
    path('properties/', property_list, name='property-list'),
]
