# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
热歌
"""

import json
import requests
import traceback

from django.http import JsonResponse
from urllib.parse import urljoin
from django.core.cache import cache
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music


class HotMusic(APIView):
    def get_hot_music(self):
        hot_music = requests.get(urljoin(NTES_URL, '/top/list'), params={'idx': 1})
        if hot_music.status_code != 200:
            return JsonResponse({"code": 500, "data": "", "error": "Get hot music error!"})
        hot_music_json = hot_music.json()['playlist']['tracks']

        final_data = []
        for music in hot_music_json:
            _tmp = {
                "music_name": music['name'],
                "ntes_id": music['id'],
                "music_auth": '/'.join([str(auth['name']) for auth in music['ar']])
            }
            try:
                _music = Music.objects.create(**_tmp)
                _music.save()
            except:
                print(traceback.format_exc())
                print('charu shibai')
                _music = Music.objects.filter(ntes_id=music['id'], music_auth=_tmp['music_auth'], music_name=music['name']).first()
            if not _music:
                continue
            _tmp['id'] = _music.id
            final_data.append(_tmp)
        cache.set('vue-music-hot', json.dumps(final_data), timeout=60 * 60 * 24 * 7)

    def get(self, request):
        if not cache.ttl('vue-music-hot'):
            self.get_hot_music()
        return JsonResponse({"code": 200, "data": json.loads(cache.get('vue-music-hot')), "error": ""},safe=False)
