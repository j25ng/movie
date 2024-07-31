import requests
import os
import pandas as pd

def gen_url(dt='20120101', url_param = {}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    for k, v in url_param.items():
        url = url + f"&{k}={v}"

    return url

def req(dt='20120101', url_param={}):
    url = gen_url(dt, url_param)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    #print(data)
    return code, data

def get_key():
    key = os.getenv("MOVIE_API_KEY")
    return key

def req2list(dt='20120101', url_param={}):
    _, data = req(dt, url_param)
    # data.get('boxOfficeResult').get('dailyBoxOfficeList')
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def list2df(dt='20120101', url_param={}):
    l = req2list(dt, url_param)
    df = pd.DataFrame(l)
    return df

def save2df(dt='20120101', url_param={}):
    df = list2df(dt, url_param)
    df['loadDt'] = dt 
   #df.to_parquet('~/tmp/test_parquet/', partition_cols=['loadDt'])
    return df

def echo(yaho):
    return yaho

def apply_type2df(load_dt='20120101', path="~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/loadDt={load_dt}')

    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']

    #for c in num_cols:
    #    df[c] = pd.to_numeric(df[c])

    df[num_cols] = df[num_cols].apply(pd.to_numeric)

    return df
