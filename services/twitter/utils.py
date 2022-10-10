from typing import Optional

from services.twitter.models import TwitterUserModel
from services.twitter.api import api


def get_twitter_info_by_name(name: str) -> Optional[TwitterUserModel]:
    return api.get_user(screen_name=name)


def get_lists_of_twitter_users(names: list[str]):
    names = set(names)
    data = []
    for name in names:
        if (person := get_twitter_info_by_name(name)) is not None:
            data.append(
                {
                    'name': person.name,
                    'id': person.id,
                    'screen_name': person.screen_name,
                    'description': person.description,
                    'followers_count': person.followers_count,
                    'following': person.following,
                }
            )
    return data


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
