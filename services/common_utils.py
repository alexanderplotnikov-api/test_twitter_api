import re

from django.shortcuts import render
from tweepy.errors import TooManyRequests


def urls_to_screen_name(text: str):
    return [
        url.split('/')[-1] if url.split('/')[-1] != '' else url.split('/')[-2]
        for url in re.findall(r'(https?://[^\s]+)', text.lower())
    ]


def too_many_request_handler(func):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except TooManyRequests as e:
            return render(request, 'error.html')

    return wrapper
