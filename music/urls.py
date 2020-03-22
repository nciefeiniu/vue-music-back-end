# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views
from .views.account import CreateUserView, Test, MyLoveMusicList, MySongSheetList
from music.views.hot import HotMusic
from music.views.search import SearchMusic
from music.views.music2url import MusicUrl

# django url
urlpatterns = [
    path('account/', CreateUserView.as_view(), name='account'),
    path('test/', Test.as_view(), name='test'),
    path('love_music/', MyLoveMusicList.as_view(), name='love_music'),
    path('song_sheet/', MySongSheetList.as_view(), name='song_sheet_list'),
    path('hot/', HotMusic.as_view(), name='hot_music'),
    path('search/', SearchMusic.as_view(), name='search_music'),
    path('song_url/', MusicUrl.as_view(), name='music_url')
]