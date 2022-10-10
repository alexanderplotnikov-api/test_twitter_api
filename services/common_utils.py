from django.shortcuts import render
from tweepy.errors import TooManyRequests


def urls_to_screen_name(urls: list[str]):
    return [url[-1] if url[-1] != '' else url[-2] for url in list(map(lambda x: x.split('/'), urls))]


def too_many_request_handler(func):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except TooManyRequests as e:
            return render(request, 'error.html')

    return wrapper
