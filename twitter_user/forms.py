from django import forms


class UserInfoForm(forms.Form):
    twitter_url = forms.URLInput()
