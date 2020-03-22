# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
get music url
"""

import requests
import traceback

from django.core.cache import cache
from django.http import JsonResponse
from urllib.parse import urljoin
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music
from music.serializers.music import MusicUrlSerializer


class MusicUrl(APIView):
    def set_music_url_cache(self, id: str, url: str):
        cache.set("vue-music-url-{ntesid}".format(ntesid=id), url, timeout=60 * 3)

    def get(self, request):
        m_id = request.GET['mid']
        music_url = Music.objects.get(pk=m_id)
        if music_url.music_url:
            serializer = MusicUrlSerializer(music_url)
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        # if not music url, it is ntes music , need request ntes API

        if not cache.ttl("vue-music-url-{ntesid}".format(ntesid=m_id)):

            ntes_resp = requests.get(urljoin(NTES_URL, '/song/url'), params={'id': music_url.ntes_id})
            if ntes_resp.status_code != 200:
                return JsonResponse({"code": 500, "data": [], "error": "Get Music url error!"})
            ntes_resp_json = ntes_resp.json()
            if ntes_resp_json['code'] != 200:
                return JsonResponse({"code": 500, "data": [], "error": "Get Music url error!"})
            self.set_music_url_cache(m_id, ntes_resp_json['data'][0]['url'])

        return JsonResponse(
            {"code": 200, "data": {"id": m_id, "music_name": music_url.music_name, "music_auth": music_url.music_auth,
                                   "music_url": cache.get("vue-music-url-{ntesid}".format(ntesid=m_id))},
             "error": ""})
