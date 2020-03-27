# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from rest_framework.views import APIView

from music.models import Music, RadioStation, RadioStationMusic
from music.views.account import AuthenticationBaseAPIView
from music.serializers.music import RadioSerializer, RadioAddMusicSerializer


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


class RadioList(APIView):
    def get(self, request):
        _radios = RadioStation.objects.all()
        serializer = RadioSerializer(_radios, many=True)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})


class RadioAddMusic(AuthenticationBaseAPIView):
    def get(self, request, rid):
        _tmp = RadioStationMusic.objects.filter(radio_station_id=rid)
        serializer = RadioAddMusicSerializer(_tmp, many=True)
        return JsonResponse({"code": 200, "data": serializer.data, "error": ""})

    def post(self, request):
        serializer = RadioAddMusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"code": 200, "data": serializer.data, "error": ""})
        return JsonResponse({"code": 500, "data": "", "error": serializer.errors})