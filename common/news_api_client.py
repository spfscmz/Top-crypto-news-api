import requests

from json import loads

NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = 'f12c81ff12224383b1f44c44a98b4dc5'
ARTICALS_API = 'articles'

CNN = 'cnn'
DEFAILT_SOURCES = [CNN]
SORT_BY_TOP = 'top'

def buildUrl(end_point=NEWS_API_ENDPOINT, api_name=ARTICALS_API):
    return end_point + api_name

def getNewsFromSource(sources=DEFAILT_SOURCES, sortBy=SORT_BY_TOP):
    articles = []
    for source in sources:
        payload = {'apiKey' : NEWS_API_KEY,
                    'source' : source,
                    'sortBy' : sortBy}
    
        response = requests.get(buildUrl(), params=payload)
        
        res_json = loads(response.content)

        print(res_json)
        
        if (res_json is not None and 
            res_json['status'] == 'ok' and
            res_json['source'] is not None):
            # populate new
            for news in res_json['articles']:
                news['source'] = res_json['source']

            articles.extend(res_json['articles'])

    return articles        
