# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2023/05/01 19:13:20
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from .models import *
from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer


class SImage(Serializer):
    image_url = serializers.ReadOnlyField()
    default_value = ""
    default_value_map = {
        "height": 0,
        "width": 0,
        "region": {},
    }

    class Meta:
        model = MImage
        fields = "__all__"


class VSImage(viewsets.ModelViewSet):
    queryset = MImage.objects.all()
    serializer_class = SImage


class SImageCollection(Serializer):
    default_value = ""

    class Meta:
        model = MImageCollection
        fields = "__all__"


class VSImageCollection(viewsets.ModelViewSet):
    queryset = MImageCollection.objects.all()
    serializer_class = SImageCollection


class SPDF(Serializer):
    default_value = ""

    class Meta:
        model = MPDF
        fields = "__all__"


class VSPDF(viewsets.ModelViewSet):
    queryset = MPDF.objects.all()
    serializer_class = SPDF


class SPDFCollection(Serializer):
    default_value = ""

    class Meta:
        model = MPDFCollection
        fields = "__all__"


class VSPDFCollection(viewsets.ModelViewSet):
    queryset = MPDFCollection.objects.all()
    serializer_class = SPDFCollection


class SPackage(Serializer):
    default_value = ""

    class Meta:
        model = MPackage
        fields = "__all__"


class VSPackage(viewsets.ModelViewSet):
    queryset = MPackage.objects.all()
    serializer_class = SPackage


class SPackageCollection(Serializer):
    default_value = ""

    class Meta:
        model = MPackageCollection
        fields = "__all__"


class VSPackageCollection(viewsets.ModelViewSet):
    queryset = MPackageCollection.objects.all()
    serializer_class = SPackageCollection


class SRequest(Serializer):
    default_value = ""

    class Meta:
        model = MRequest
        fields = "__all__"


class VSRequest(viewsets.ModelViewSet):
    queryset = MRequest.objects.all()
    serializer_class = SRequest


class SResponse(Serializer):
    default_value = ""

    class Meta:
        model = MResponse
        fields = "__all__"


class VSResponse(viewsets.ModelViewSet):
    queryset = MResponse.objects.all()
    serializer_class = SResponse


class SHTMLFile(Serializer):
    default_value = ""

    class Meta:
        model = MHTMLFile
        fields = "__all__"


class VSHTMLFile(viewsets.ModelViewSet):
    queryset = MHTMLFile.objects.all()
    serializer_class = SHTMLFile


class SVideoCollection(Serializer):
    default_value = ""

    class Meta:
        model = MVideoCollection
        fields = "__all__"


class VSVideoCollection(viewsets.ModelViewSet):
    queryset = MVideoCollection.objects.all()
    serializer_class = SVideoCollection


class SVideo(Serializer):
    default_value = ""

    class Meta:
        model = MVideo
        fields = "__all__"


class VSVideo(viewsets.ModelViewSet):
    queryset = MVideo.objects.all()
    serializer_class = SVideo


class SAudioCollection(Serializer):
    default_value = ""

    class Meta:
        model = MAudioCollection
        fields = "__all__"


class VSAudioCollection(viewsets.ModelViewSet):
    queryset = MAudioCollection.objects.all()
    serializer_class = SAudioCollection


class SAudio(Serializer):
    default_value = ""

    class Meta:
        model = MAudio
        fields = "__all__"


class VSAudio(viewsets.ModelViewSet):
    queryset = MAudio.objects.all()
    serializer_class = SAudio


class STextCollection(Serializer):
    default_value = ""

    class Meta:
        model = MTextCollection
        fields = "__all__"


class VSTextCollection(viewsets.ModelViewSet):
    queryset = MTextCollection.objects.all()
    serializer_class = STextCollection


class SText(Serializer):
    default_value = ""

    class Meta:
        model = MText
        fields = "__all__"


class VSText(viewsets.ModelViewSet):
    queryset = MText.objects.all()
    serializer_class = SText
