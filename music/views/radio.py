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

from music.models import Music, SongSheet, SongSheetMusic, RadioStation
from music.serializers.account import SongSheetListSerializer
from music.views.account import AuthenticationBaseAPIView
from music.serializers.music import AddMusic2SongSheetSerializer, SongSheetMusicsSerializer, UploadMusicSerializer, RadioSerializer


class Radio(AuthenticationBaseAPIView):
    def get(self, request):
        _radios = RadioStation.objects.filter(user_id=request.user.id)
        serializer = RadioSerializer(_radios, many=True)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})

    def post(self, request):
        serializer = RadioSerializer(data={**request.data, **{"user_id": request.user.id}})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        return JsonResponse({"code": 500, "data": "", "error": serializer.errors})