# !/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from music.models import UploadImages


class UploadImageSerializer(serializers.ModelSerializer):
    relative_url = serializers.CharField(source='file', default='')

    class Meta:
        model = UploadImages
        fields = '__all__'