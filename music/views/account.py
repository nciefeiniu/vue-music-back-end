# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback

from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model  # If used custom user model

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler

from music.serializers.account import *
from music.models import *


# 创建用户
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class AuthenticationBaseAPIView(APIView):
    # 认证基础类
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class Test(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self):
        return Response("afawf")


class MyLoveMusicList(AuthenticationBaseAPIView):
    """
    我喜欢的歌 相关功能API
    """
    def get(self, request):
        # print(request.user.id)
        my_love_music = MyLoveMusic.objects.filter(user_id=request.user.id)
        my_love_music_data = MyLoveMusicSerializer(my_love_music, many=True)
        return JsonResponse({"code": 200, "data": my_love_music_data.data, "error": ""})

    def post(self, request):
        # 增加歌曲到我喜欢里面
        print(request.data, request.user.id)
        try:
            mlm = MyLoveMusic(user_id=request.user, music_id_id=request.data['id'])
            mlm.save()
            return JsonResponse({"code": 200, "data": 'ok', "error": ""})
        except:
            print(traceback.format_exc())
            return JsonResponse({"code": 500, "data": "", "error": "ERROR"})


class MySongSheetList(AuthenticationBaseAPIView):
    """
    我创建的歌单列表
    """
    def get(self, request):
        my_song_sheet_list = SongSheet.objects.filter(user_id=request.user.id)
        serializer = SongSheetListSerializer(my_song_sheet_list)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})


class MySongSheet(AuthenticationBaseAPIView):
    """
    我的歌单
    """
    def post(self, request):
        """
        新建歌单
        :param request:
        :return:
        """
        serializer = SongSheetSerializer(**{**request.data, **{"user_id": request.user.id}})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        return JsonResponse({"code": 500, "data": serializer.errors, "error": ""})
