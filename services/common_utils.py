def urls_to_screen_name(urls: list[str]):
    return [url[-1] if url[-1] != '' else url[-2] for url in list(map(lambda x: x.split('/'), urls))]

