# !/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from music.models import UploadImages


class UploadImageSerializer(serializers.ModelSerializer):
    # file = serializers.CharField()
    relative_url = serializers.CharField(source='file')

    class Meta:
        model = UploadImages
        fields = '__all__'