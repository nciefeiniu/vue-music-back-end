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


class SongSheetMusicsSerializer(serializers.ModelSerializer):
    music_name = serializers.CharField(source="music_id.music_name")
    music_auth = serializers.CharField(source="music_id.music_auth")
    id = serializers.IntegerField(source="music_id.id")

    class Meta:
        model = SongSheetMusic
        fields = "__all__"


class AddMusic2SongSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongSheetMusic
        fields = ('id', "music_id", "song_sheet_id")


class SongSheetMusicsSerializer(serializers.ModelSerializer):
    music_name = serializers.CharField(source="music_id.music_name")
    music_auth = serializers.CharField(source="music_id.music_auth")
    id = serializers.IntegerField(source="music_id.id")

    class Meta:
        model = SongSheetMusic
        fields = "__all__"


class UploadMusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadMuisc
        fields = "__all__"


class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioStation
        fields = "__all__"