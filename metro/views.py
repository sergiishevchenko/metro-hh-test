import requests
from django.shortcuts import render
from config import access_token

def hh_metro(request):
    result = requests.get('https://api.hh.ru/metro/4').json()
    auth = requests.get('https://hh.ru/oauth/authorize?response_type=code&token={}'.format(access_token))
    result_from_auth = requests.get('https://api.hh.ru/metro/4').json()

    new = []
    old = []
    deleted = []
    for item_auth in result_from_auth['lines']:
        for item in result['lines']:
            if len(item['stations']) == len(item_auth['stations']):
                for k in item['stations']:
                    old.append(k['name'])
            else:
                if len(item['stations']) < len(item_auth['stations']):
                    mid = []
                    for w in item_auth['stations']:
                        mid.append(w['name'])
                    for j in item['stations']:
                        if j['name'] not in mid:
                            new.append(j['name'])
                else:
                    mid = []
                    for w in item_auth['stations']:
                        mid.append(w['name'])
                    for j in item['stations']:
                        if j['name'] not in mid:
                            deleted.append(j['name'])
    return render(request, 'hh_metro.html', {'new': new, 'old': old, 'deleted': deleted})
