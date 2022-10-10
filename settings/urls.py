"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from twitter_user.views import get_smt, get_users_info, get_user_tweets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_smt, name='index'),
    path('table/', get_users_info, name='user_info'),
    path(r'table/last_tweets/(?P<person_id>[0-9]+)$', get_user_tweets, name='last_tweets'),
]
