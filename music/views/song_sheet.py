# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback

from django.http import JsonResponse
from urllib.parse import urljoin
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music, SongSheet, SongSheetMusic
from music.serializers.account import SongSheetListSerializer
from music.views.account import AuthenticationBaseAPIView
from music.serializers.music import AddMusic2SongSheetSerializer


class PublickSongSheets(APIView):
    def get(self, request):
        my_song_sheet_list = SongSheet.objects.order_by('?').filter(is_public=True)[:8]
        serializer = SongSheetListSerializer(my_song_sheet_list, many=True)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})


class AddMusic2SongSheet(AuthenticationBaseAPIView):
    def post(self, request):
        if 'music_id' not in request.data:
            return JsonResponse({"code": 500, "data": "", "error": "keywords 'music_id' can not empty"})

        if 'song_sheet_id' not in request.data:
            return JsonResponse({"code": 500, "data": "", "error": "keywords 'song_sheet_id' can not empty"})

        serializer = AddMusic2SongSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        return JsonResponse({"code": 500, "data": serializer.errors, "error": ""})