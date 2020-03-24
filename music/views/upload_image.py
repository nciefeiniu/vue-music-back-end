# !/usr/bin/env python
# -*- coding: utf-8 -*-


from rest_framework import viewsets

from music.models import UploadImages
from music.serializers.upload_image import UploadImageSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = UploadImages.objects.all()
    serializer_class = UploadImageSerializer
