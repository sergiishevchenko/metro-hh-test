import requests
from django.shortcuts import render


def hh_metro(request):
    result = requests.get('https://api.hh.ru/metro/1').json()
    # print(result)
    # auth = requests.get('https://hh.ru/oauth/authorize?response_type=code&client_id=token')
    # result_from_auth = requests.get('https://api.hh.ru/metro/1').json()

    # result = {'id': '3', 'name': 'Екатеринбург', 'lines': [{'id': '48', 'hex_color': '0A6F20', 'name': 'Север-Юг', 'stations': [
    #     {'id': '48.261', 'name': 'Проспект Космонавтов', 'lat': 56.900393, 'lng': 60.613878, 'order': 0}, 
    #     {'id': '48.265', 'name': 'Динамо', 'lat': 56.847818, 'lng': 60.599406, 'order': 4}, 
    #     {'id': '48.266', 'name': 'Площадь 1905 года', 'lat': 56.837982, 'lng': 60.59734, 'order': 5}, 
    #     {'id': '48.267', 'name': 'Геологическая', 'lat': 56.826715, 'lng': 60.603754, 'order': 6}, 
    #     {'id': '48.268', 'name': 'Бажовская', 'lat': 56.837982, 'lng': 60.59734, 'order': 7}, 
    #     {'id': '48.269', 'name': 'Чкаловская', 'lat': 56.808502, 'lng': 60.610698, 'order': 8}, 
    #     {'id': '48.270', 'name': 'Ботаническая', 'lat': 56.797487, 'lng': 60.633362, 'order': 9}]}]}
    result_from_auth = {'id': '3', 'name': 'Екатеринбург', 'lines': [{'id': '48', 'hex_color': '0A6F20', 'name': 'Север-Юг', 'stations': [
        {'id': '48.261', 'name': 'Проспект Космонавтов', 'lat': 56.900393, 'lng': 60.613878, 'order': 0}, 
        {'id': '48.265', 'name': 'Динамо', 'lat': 56.847818, 'lng': 60.599406, 'order': 4}, 
        {'id': '48.266', 'name': 'Площадь 1905 года', 'lat': 56.837982, 'lng': 60.59734, 'order': 5}, 
        {'id': '48.262', 'name': 'Уралмаш', 'lat': 56.887674, 'lng': 60.614165, 'order': 1}, 
        # {'id': '48.263', 'name': 'Машиностроителей', 'lat': 56.878517, 'lng': 60.61218, 'order': 2}, 
        {'id': '48.264', 'name': 'Уральская', 'lat': 56.858056, 'lng': 60.600816, 'order': 3}, 
        {'id': '48.270', 'name': 'Ботаническая', 'lat': 56.797487, 'lng': 60.633362, 'order': 9}]}]}

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
