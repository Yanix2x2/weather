import requests


URL = 'https://wttr.in'


def get_weather(place, payload):
    url = f'{URL}/{place}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    places = [
        {"place": "london", "payload": {"nTqu": "", "lang": "en"}}, 
        {"place": "svo", "payload": {"nTqu": "", "lang": "en"}},
        {"place": "череповец", "payload": {"nTqM": "", "lang": "ru"}},
    ]

    for location in places:
        payload = location.get('payload')
        place = location.get('place') 
        print(get_weather(place, payload))


if __name__ == '__main__':
    main()
