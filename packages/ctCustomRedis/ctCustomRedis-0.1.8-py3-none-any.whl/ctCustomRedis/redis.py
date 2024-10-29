import inspect
import json
import os
from functools import wraps

from ctCustomRedis.redisConnection import get_redis_connection


def get_nested_attribute_value(obj, attr_path):
    """
    Retrieves the value of a nested attribute from an object or json.
    Args:
        obj: The object from which to retrieve the attribute.
        attr_path: The path of nested attributes.
    Returns:
        The value of the nested attribute if found, None otherwise.
    """
    attrs = attr_path.split('.')
    attr_val = obj
    for attr in attrs:
        if hasattr(attr_val, attr):
            attr_val = getattr(attr_val, attr)
        elif isinstance(attr_val, dict) and attr in attr_val:
            attr_val = attr_val[attr]
        else:
            raise Exception(attr + ' not found in the hash_field or cache_key')
    return attr_val


_request_context_accessor = None


def set_request_context_accessor(accessor_func):
    global _request_context_accessor
    _request_context_accessor = accessor_func


def get_request_context():
    if _request_context_accessor is None:
        raise RuntimeError("Request context accessor is not set.")
    return _request_context_accessor()


class CacheContext:
    def __init__(self, logger, redis_pool):
        self.logger = logger
        self.redis_pool = redis_pool
        self.client_name = client_name = redis_pool.connection_kwargs.get("client_name")


def ct_redis_cache(template_cache_key, field, expire_time=None, is_global=False, cache_enabled=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_context = get_request_context()
            use_cache = kwargs.pop('use_cache', True)

            if not cache_enabled or not use_cache:
                return func(*args, **kwargs)

            try:
                if cache_context.redis_pool and not hasattr(cache_context, 'redis_conn'):
                    redis_conn = get_redis_connection(cache_context.redis_pool)
                    pipe = redis_conn.pipeline()
                    pipe.multi()
                    cache_context.pipe = pipe
                    cache_context.redis_conn = redis_conn
                generated_cache_key, hash_field = generate_cache_key_and_hash_field(template_cache_key, func, field,
                                                                                    is_global, cache_context.client_name,
                                                                                    *args)

                hash_value_from_cache = cache_context.redis_conn.hget(generated_cache_key, hash_field)
                if hash_value_from_cache is not None:
                    print('from cache')
                    return json.loads(hash_value_from_cache)
                else:
                    func_output = func(*args, **kwargs)
                    if func_output != {}:
                        cache_context.pipe.hset(generated_cache_key, hash_field, json.dumps(func_output))
                        cache_context.pipe.expire(generated_cache_key,
                                      expire_time)
                    print('from db')
                    return func_output
            except TypeError as error:
                    cache_context.logger.info("Caught exception from cache  :: {}".format(error))
                    return func_output if func_output is not None else func(*args, **kwargs)
            except Exception as error:
                cache_context.logger.info("Caught exception from cache :: {}".format(error))
                return func(*args, **kwargs)

        return wrapper

    return decorator



def generate_cache_key_and_hash_field(template_cache_key, func, template_hash_field, is_global, cache_client_name,
                                      *args):
    env = os.getenv("ENVIRONMENT").lower()
    # get full args from the function
    arg_values = dict(zip(inspect.getfullargspec(func).args, args))
    cache_key = template_cache_key  # ':$abc.xyz'
    for arg_name, arg_value in arg_values.items():
        placeholder_start = f':${arg_name}.'  # ':$abc.'
        while placeholder_start in cache_key:
            key_start = cache_key.find(placeholder_start) + len(placeholder_start)  # key starting length
            key_end = cache_key.find(':', key_start)  # key ending length
            key_placeholder = cache_key[key_start:key_end] if key_end != -1 else cache_key[
                                                                                 key_start:]  # xyz from $abc.xyz
            if key_placeholder:
                attr_value = get_nested_attribute_value(arg_value, key_placeholder)  # value of abc.xyz
                cache_key = cache_key.replace(f'${arg_name}.{key_placeholder}',
                                              str(attr_value) if attr_value is not None else 'None')
            else:
                break
        # Replace the cache key name with value if there is not nested attribute
        cache_key = cache_key.replace(f':${arg_name}', f':{arg_value}')

    hash_field = get_nested_attribute_value(arg_values, template_hash_field.split('$', 1)[1]) \
        if '$' in template_hash_field else template_hash_field
    hash_field = str(hash_field) if hash_field is not None else template_hash_field.split('$')[1].split('.')[0]

    env = '' if env == 'prod' else env + ':'
    cache_key = f"{env}{cache_key}" if is_global else f"{env}{cache_client_name}:{cache_key}"
    return cache_key, str(hash_field)