# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework import routers

from . import views
from .views.account import CreateUserView, Test, MyLoveMusicList, MySongSheetList, MySongSheet
from music.views.hot import HotMusic
from music.views.search import SearchMusic
from music.views.music2url import MusicUrl
from music.views.upload_image import FileViewSet
from music.views.song_sheet import PublickSongSheets, AddMusic2SongSheet


router = routers.DefaultRouter()
router.register(r'upload_image', FileViewSet)

# django url
urlpatterns = [
    path('account/', CreateUserView.as_view(), name='account'),
    path('test/', Test.as_view(), name='test'),
    path('love_music/', MyLoveMusicList.as_view(), name='love_music'),
    path('song_sheets/', MySongSheetList.as_view(), name='song_sheet_list'),
    path('hot/', HotMusic.as_view(), name='hot_music'),
    path('search/', SearchMusic.as_view(), name='search_music'),
    path('song_url/', MusicUrl.as_view(), name='music_url'),
    path('song_sheet/', MySongSheet.as_view(), name='my_song_sheet'),
    path('public_song_sheet/', PublickSongSheets.as_view(), name="publick_song_sheet"),
    path('songsheet/music/', AddMusic2SongSheet.as_view(), name="songsheet_music"),
    path('', include(router.urls))
]