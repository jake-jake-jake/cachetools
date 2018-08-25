from cachetools.caches import DictCache

NUMBER_OF_CALLS = 0

def do_a_call():
    global NUMBER_OF_CALLS
    NUMBER_OF_CALLS += 1
    return 'value'

def test_cache():
    global NUMBER_OF_CALLS
    assert NUMBER_OF_CALLS == 0
    
    # init cache and give it both callables and values
    c = DictCache(10)
    c['key'] = do_a_call
    c['another key'] = 5
    assert NUMBER_OF_CALLS == 0
    
    # ensure that callable returns right value
    assert c['key'] == 'value'
    assert c['another key'] == 5
    assert NUMBER_OF_CALLS == 1

    # ensure that fetching the value again does not cause another function call
    assert c['key'] == 'value'
    assert NUMBER_OF_CALLS == 1

    # reset cache and then assert that we call function again
    c.reset()
    assert NUMBER_OF_CALLS == 1
    assert c['key'] == 'value'
    assert NUMBER_OF_CALLS == 2

