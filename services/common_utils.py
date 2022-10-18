import re


def urls_to_screen_name(text: str):
    return [
        url.split('/')[-1] if url.split('/')[-1] != '' else url.split('/')[-2]
        for url in re.findall(r'(https?://[^\s]+)', text.lower())
    ]
