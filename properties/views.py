from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from properties.models import Property


@cache_page(60 * 15)
def property_list(request):
    """
    Function-based view to handle property listings with caching.
    """
    properties = Property.objects.all().values()
    data = list(properties)

    return JsonResponse({"data": data})
