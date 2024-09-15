import requests
import os

AUTH = os.environ['AUTH']
DEVICE = os.environ['DEVICE_TOKEN']
PHPSESSID = os.environ['PHPSESSID']

cookies = {
    'PHPSESSID': PHPSESSID,
}

headers = {
    'accept-language': 'en;q=1.0',
    'user-agent': 'USCAPP/5.7.1 (android; 34; Scale/2.625)',
    'device-token': DEVICE,
    'device-name': 'Pixel 7a',
    'authorization': AUTH,
    'Host': 'api.urbansportsclub.com',
    'Connection': 'Keep-Alive',
}


def get_venue():
    response = requests.get('https://api.urbansportsclub.com/api/v6/venues/24015', cookies=cookies, headers=headers)
    return response.json()


def get_scheduled_bookings():
    params = {
        'type': 'schedule',
        'pageSize': '20',
        'page': '1',
    }

    response = requests.get(
        'https://api.urbansportsclub.com/api/v6/bookings',
        params=params,
        cookies=cookies,
        headers=headers
    )
    return response.json()

def get_classes(start_date):
    params = {
        'forDurationOfDays': '1',
        'query': '',
        'pageSize': '100',
        'page': '1',
        'locationId': '24015',
        'startDate': start_date,
    }

    response = requests.get(
        'https://api.urbansportsclub.com/api/v6/courses',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.json()

def get_class(class_id):
    response = requests.get(
        f'https://api.urbansportsclub.com/api/v6/courses/{class_id}',
        cookies=cookies,
        headers=headers,
    )
    return response.json()

def book_class(class_id):
    data = {
        'courseId': class_id,
    }

    response = requests.post(
        'https://api.urbansportsclub.com/api/v6/bookings',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.json()