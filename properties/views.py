from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from properties.utils import get_all_properties


def property_list(request):
    """
    Function-based view to handle property listings with caching.
    """
    data = list(get_all_properties())

    return JsonResponse({"data": data})
