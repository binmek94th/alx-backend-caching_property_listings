from django.http import JsonResponse
from rest_framework.response import Response

from properties.models import Property
from properties.serializers import PropertyListingSerializer


def property_list(request):
    """
    Function-based view to handle property listings with caching.
    """
    properties = Property.objects.all()
    return JsonResponse(properties, safe=False)
