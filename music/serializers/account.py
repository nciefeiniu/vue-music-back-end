# !/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

from music.models import *

# 获取用户模块model
UserModel = get_user_model()


# 创建用户
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", "email")


class MyLoveMusicSerializer(serializers.ModelSerializer):
    music_name = serializers.CharField(source="music_id.music_name")
    music_auth = serializers.CharField(source="music_id.music_auth")
    id = serializers.IntegerField(source='music_id.id')

    class Meta:
        model = MyLoveMusic
        fields = "__all__"
        # read_only_fields = ('id', 'music_name', 'music_auth')


class SongSheetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongSheet
        fields = "__all__"


class SongSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongSheet
        fields = ("id", "sheet_name", "user_id", "img_url", "song_sheet_desc", "is_public")
