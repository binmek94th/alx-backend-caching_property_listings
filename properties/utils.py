from django.core.cache import cache


def get_all_properties():
    """
    Get all properties from the properties module.
    """
    properties = cache.get('all_properties')
    if properties is None:
        from properties.models import Property
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)
        return queryset
    return properties
