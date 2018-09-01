# cachetools
Useful pythonic classes for lazily caching expensive lookups.

## Installation
By cloning the repo and installing via `setup.py`

## Usage
```
# add items to the cache as if it were a dict
d = DictCache(10)
an_api_call = partial(requests.get, "a slow api endpoint")
d['an api call'] = an_api_call

# check contents like a dict
'an api call' in d  # True

# only execute function on key lookup
data = d['an api call']  # partial function is called (but only once)

# store result of function
data2 = d['an api call']  # partial function not called again; result is cached

# reset cache
d.reset('an api call')

```
