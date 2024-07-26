def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "c86077f6d23d4527443b5460a7a1c90b"

    url = f"{base_url}?key={key}&targetDT={dt}"
    print(url)
