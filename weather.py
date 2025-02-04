import requests


URL = 'https://wttr.in'


def get_weather(place, payload):
    url = f'{URL}/{place}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    london_weather = get_weather(
        "london",
        {
            'nTqu': '',
            'lang': 'en',
        },
    )
    print(london_weather)

    svo_weather = get_weather(
        "svo",
        {
            'nTqu': '',
            'lang': 'en',
        },

    )
    print(svo_weather)

    cherepovets_weather = get_weather(
        "череповец",
        {
            'nTqM': '',
            'lang': 'ru',
        },
    )
    print(cherepovets_weather)


if __name__ == '__main__':
    main()
