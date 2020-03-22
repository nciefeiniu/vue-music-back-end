# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback

from django.http import JsonResponse
from urllib.parse import urljoin
from rest_framework.views import APIView
from django_backend.settings import NTES_URL

from music.models import Music


class SearchMusic(APIView):
    def search_music_ntes(self, key_word):
        ntes_resp = requests.get(urljoin(NTES_URL, '/search'), params={'keyword': key_word}, timeout=30)
        if ntes_resp.status_code != 200:
            return JsonResponse({"code": 500, "data": "", "error": "Search music error!"})
        ntes_resp_json = ntes_resp.json()

        final_data = []
        for music in ntes_resp_json['result']['songs']:
            _tmp = {
                "music_name": music['name'],
                "ntes_id": music['id'],
                "music_auth": '/'.join([str(auth['name']) for auth in music['artists']])
            }
            final_data.append(_tmp)
            try:
                music = Music.objects.create(**_tmp)
                music.save()
            except:
                print(traceback.format_exc())
                print('charu shibai')
        return JsonResponse({"code": 200, "data": final_data, "error": ""})

    def search_music(self, key_word):
        db_result = Music.objects.filter(music_name__contains=key_word)
        if not db_result:
            return self.search_music_ntes(key_word)
        final_data = []

        for music in db_result:
            final_data.append({
                "music_name": music.music_name,
                "ntes_id": music.ntes_id,
                "music_auth": music.music_auth
            })
        return JsonResponse({"code": 200, "data": final_data, "error": ""})

    def get(self, request):
        _kw = request.GET['keyword']
        if not _kw:
            return JsonResponse({"code": 500, "data": "", "error": "keyword can not be empty"})
        return self.search_music(_kw)
