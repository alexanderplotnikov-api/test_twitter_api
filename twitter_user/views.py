from django.http import HttpResponse
from django.template import loader

from services.common_utils import urls_to_screen_name, too_many_request_handler
from services.twitter.utils import get_lists_of_twitter_users, get_last_tweets_by_username


def get_index_page(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@too_many_request_handler
def get_users_info(request):
    template = loader.get_template('table.html')
    context = {}
    users_name = urls_to_screen_name(request.POST.getlist('urls'))
    users_data, errors = get_lists_of_twitter_users(users_name)
    context['persons'] = users_data
    context['errors'] = errors
    return HttpResponse(template.render(context, request))


@too_many_request_handler
def get_user_tweets(request, person_id):
    template = loader.get_template('tweets.html')
    tweets = get_last_tweets_by_username(person_id)
    context = {}
    context['tweets'] = tweets
    return HttpResponse(template.render(context, request))
