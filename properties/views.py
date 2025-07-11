from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView

from properties.models import Property
from properties.serializers import PropertyListingSerializer


class PropertiesView(APIView):
    """
    View to handle property listings.
    """

    @cache_page(60 * 15)
    def get(self, request):
        """
        Handle GET requests to retrieve property listings.
        """
        properties = Property.objects.all()
        serializer = PropertyListingSerializer(properties, many=True)
        return Response(serializer.data, status=200)
