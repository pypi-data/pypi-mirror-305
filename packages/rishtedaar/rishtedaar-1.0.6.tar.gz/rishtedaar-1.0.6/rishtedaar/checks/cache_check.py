import warnings
import logging

def check_cache(cache_alias='default', test_key='health_check_key', test_value='health_check_value'):
    from django.core.cache import caches
    from django.core.cache.backends.base import CacheKeyWarning
    try:
        warnings.simplefilter("ignore", CacheKeyWarning)
        cache = caches[cache_alias]
        cache.get('_health_check')
        logging.info("Cache is healthy")
        return True, "Cache is healthy"
    except Exception as e:
        logging.error(f"Cache health check failed: {str(e)}")
        return False, f"Cache error: {str(e)}"
