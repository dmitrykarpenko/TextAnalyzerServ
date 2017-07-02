from django.conf.urls import url

from .api import UserApi, UserTextApi

urlpatterns = [
    url(r'^users$', UserApi.as_view()),
    url(r'^usertexts$', UserTextApi.as_view()),
]
