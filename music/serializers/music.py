# !/usr/bin/env python
# -*- coding: utf-8 -*-


from rest_framework import serializers

from music.models import *


class SearchMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'music_name', 'music_auth', 'music_url')
        read_only_fields = ('id',)


class MusicUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'music_name', 'music_auth', 'music_url')
        read_only_fields = ('id',)


class AddMusic2SongSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongSheetMusic
        fields = ('id', "music_id", "song_sheet_id")
