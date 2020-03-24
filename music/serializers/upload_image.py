# !/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from music.models import UploadImages


class UploadImageSerializer(serializers.ModelSerializer):
    file = serializers.CharField()

    class Meta:
        model = UploadImages
        fields = '__all__'