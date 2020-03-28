# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import traceback

from django.http import JsonResponse

from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from django.contrib.auth import get_user_model  # If used custom user model

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler

from music.serializers.account import *
from music.models import *


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# 创建用户
class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        payload = jwt_payload_handler(User.objects.get(pk=serializer.data.get('id')))
        token = jwt_encode_handler(payload)
        data = serializer.data
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


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
        serializer = SongSheetListSerializer(my_song_sheet_list, many=True)
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
        print(request.data)
        serializer = SongSheetSerializer(data={**request.data, **{"user_id": request.user.id}})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        return JsonResponse({"code": 500, "data": serializer.errors, "error": ""})
