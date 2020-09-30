import requests
from django.shortcuts import render
from config import access_token

def hh_metro(request):
    result = requests.get('https://api.hh.ru/metro/1').json()
    headers = {'Authorization': 'Bearer {}'.format(access_token), 'User-Agent': 'api-test-agent'}
    result_from_auth = requests.get('https://api.hh.ru/metro/1', headers=headers, verify=False).json()

    new = []
    old = []
    deleted = []
    for line_auth in result_from_auth['lines']:
        for line in result['lines']:
            if line['name'] == line_auth['name']:
                r = []
                for station in line['stations']:
                    r.append(station['name'])
                for station_auth in line_auth['stations']:
                    if station_auth['name'] in r:
                        old.append(station_auth['name'])
                    elif station_auth['name'] not in r:
                        new.append(station_auth['name'])
    return render(request, 'hh_metro.html', {'new': new, 'old': old, 'deleted': deleted})
