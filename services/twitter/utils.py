from services.twitter.api import api


def get_twitter_info_by_names(name):
    return api.lookup_users(screen_name=name)


def get_chunked_list(values, size):
    for i in range(0, len(values), size):
        yield values[i:i + size]


def get_lists_of_twitter_users(names):
    names = list(set(names))
    data = []
    errors = []
    for chunk_of_names in get_chunked_list(names, 100):
        data.extend(
            [
                {
                    'name': person.name,
                    'id': person.id,
                    'screen_name': person.screen_name,
                    'description': person.description,
                    'followers_count': person.followers_count,
                    'following': person.friends_count,
                }
                for person
                in get_twitter_info_by_names(chunk_of_names)
            ]
        )

    #  Notify user when twitter account not founded
    if len(data) != len(names):
        finded_names = tuple(p.get('screen_name').lower() for p in data)
        errors = [f'Twitter account "{name}" not found' for name in names if name.lower() not in finded_names]

    return data, errors


def get_last_tweets_by_username(person_id: int):
    return [
        {
            'id': tweet.id,
            'text': tweet.full_text,
            'retweet_count': tweet.retweet_count
        }
        for tweet
        in api.user_timeline(user_id=person_id, count=10, tweet_mode='extended')
    ]
