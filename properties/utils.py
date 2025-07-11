import logging

from django.core.cache import cache
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)


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


def get_redis_cache_metrics():
    """
    Get Redis cache metrics and calculate hit ratio.
    """
    redis_conn = get_redis_connection("default")
    hits = int(redis_conn.info().get("keyspace_hits", 0))
    misses = int(redis_conn.info().get("keyspace_misses", 0))

    total_requests = hits + misses
    hit_ratio = hits / total_requests if total_requests > 0 else 0

    metrics = {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio
    }

    logger.error(metrics)
    return metrics
