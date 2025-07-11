from rest_framework import serializers

from properties.models import Property


class PropertyListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
