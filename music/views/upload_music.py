# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
import traceback

from datetime import datetime
from django.http import JsonResponse
from django.db import transaction
from urllib.parse import urljoin
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music, SongSheet, SongSheetMusic
from music.serializers.account import SongSheetListSerializer
from music.views.account import AuthenticationBaseAPIView
from music.serializers.music import AddMusic2SongSheetSerializer, SongSheetMusicsSerializer, UploadMusicSerializer


class UploadMusic(AuthenticationBaseAPIView):
    @transaction.atomic
    def post(self, request):
        file = request.FILES.get("file", None)
        if not file:
            return JsonResponse({"code": 400, "error": "file can not empty"})

        file_name = "{time}_{origin_name}".format(origin_name=file.name, time=datetime.now().strftime("%Y-%m-%d_%H:%M%S"))
        destination = open(os.path.join("static/uploads/", file_name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        print(request.data)
        print(request.data['music_name'], request.data['music_auth'])
        music_info = {**request.data, **{'user': request.user.id, 'path': "static/uploads/{name}".format(name=file_name)}}
        music_info['music_name'] = music_info['music_name'][0]
        music_info['music_auth'] = music_info['music_auth'][0]
        # music_info['file'] = music_info['file'][0]
        serilizer = UploadMusicSerializer(data=music_info)
        if serilizer.is_valid():
            serilizer.save()
            # return JsonResponse({"code": 200, "data": serilizer.data, 'error': ""})
        else:
            return JsonResponse({"code": 200, "data": "", 'error': serilizer.errors})
        music = Music(music_name=request.data['music_name'], music_auth=request.data['music_auth'],
                      music_url=serilizer.data.get('path'))
        print(serilizer.data.get('path'))
        music.save()

        _data = {"music_name": music.music_name, "music_auth": music.music_auth,
                                                   "music_url": music.music_url, "id": music.id}
        print(_data)

        return JsonResponse({"code": 200, "data": _data, 'error': ""})
