from movie.api.call import gen_url, req, get_key, req2dataframe

def test_hide_key():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200

def test_req2():
    l = req2dataframe()
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'
