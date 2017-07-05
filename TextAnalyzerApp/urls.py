from django.conf.urls import url
from django.views.generic import TemplateView

from .api import UserApi, UserTextApi

urlpatterns = [
    # api
    url(r'^users$', UserApi.as_view()),
    url(r'^usertexts$', UserTextApi.as_view()),

    # pages
    url(r'^home', TemplateView.as_view(template_name="TextAnalyzer/home.html")),
]
