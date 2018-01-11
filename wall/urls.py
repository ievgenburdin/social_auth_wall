from django.conf.urls import url
from wall.views import Wall, MessageCreate, CommentCreate, NextPage


urlpatterns = [
    url(r'^$', Wall.as_view(), name='wall'),
    url(r'^message/create/$', MessageCreate.as_view(), name='message_create'),
    url(r'^comment/create/$', CommentCreate.as_view(), name='comment_create'),
    url(r'^next/$', NextPage.as_view(), name='next_page'),
    ]


