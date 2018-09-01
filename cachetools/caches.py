try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

from functools import partial


def make_func(func, *args, **kwargs):
    return partial(func, *args, **kwargs)


class DictCache(MutableMapping):
    """ Cache class that presents itself like a dict. On key assignment, if value is a callable,
        it will only be called on key look up."""
    
    def __init__(self, *args, **kwargs):
        self._cache = {}

    def __getitem__(self, key):
        if key in self._cache:
            func_or_val, fetched = self._cache[key]
            if fetched is None:
                fetched = func_or_val.__call__() if hasattr(func_or_val, '__call__') else func_or_val
                self._cache[key] = func_or_val, fetched
            return fetched
        else:
            raise KeyError

    def __setitem__(self, key, value):
        self._cache[key] = value, None

    def __delitem__(self, key):
        del self._cache[key]

    def __len__():
        return len(self._cache)

    def __iter__(self):
        return iter(self._cache)

    def reset(self, key=None):
        """ Remove stored values from cache. """
        if key is not None:
            if key not in self:
                raise KeyError('Key not in Cache: %s' % key)
            tup = self._cache[key]
            self._cache[key] = tup[0], None
            return
        
        for key, tup in self._cache.items():
            self._cache[key] = tup[0], None

