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


def get_redis_cache_metrics():
    """
    Get Redis cache metrics.
    """
    from django_redis import get_redis_connection
    redis_conn = get_redis_connection("default")

    hit = redis_conn.conn.info("keyspace")['db0']['keys']
    miss = redis_conn.conn.info("keyspace")['db0']['expires']
    calculated_metrics = hit / (hit + miss)
    metrics = {
        "hit_count": redis_conn.info("keyspace")['db0']['keys'],
        "miss_count": redis_conn.info("keyspace")['db0']['expires'],
        "calculated_metrics": calculated_metrics
    }
    print(calculated_metrics)
    return metrics
