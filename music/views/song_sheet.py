# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback

from django.http import JsonResponse
from urllib.parse import urljoin
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music, SongSheet
from music.serializers.account import SongSheetListSerializer


class PublickSongSheets(APIView):
    def get(self, request):
        my_song_sheet_list = SongSheet.objects.order_by('?').filter(is_public=True)[:8]
        serializer = SongSheetListSerializer(my_song_sheet_list, many=True)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})