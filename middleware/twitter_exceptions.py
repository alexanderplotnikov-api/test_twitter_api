import tweepy.errors as errors
from django.middleware.common import MiddlewareMixin
from django.shortcuts import render


#  INFO: some loggers can be placed here
class ErrorMiddleware(MiddlewareMixin):
    pass
    # def process_exception(self, request, exception):
    #     error_message = 'Something went wrong, please try later'
    #     if isinstance(exception, errors.TooManyRequests):
    #         error_message = 'Too many Twitter requests, please try later'
    #     elif isinstance(exception, errors.TwitterServerError):
    #         error_message = 'Twitter server unavailable, please try later'
    #     elif isinstance(exception, errors.Unauthorized):
    #         error_message = 'Twitter credential not provided'
    #     elif isinstance(exception, errors.BadRequest):
    #         error_message = 'Incorrect request data, please check the entered data'
    #     elif isinstance(exception, errors.Forbidden):
    #         error_message = 'Twitter action forbidden'
    #     elif isinstance(exception, errors.NotFound):
    #         error_message = 'Twitter found nothing'
    #     return render(request, 'error.html', context={'error_msg': error_message})
