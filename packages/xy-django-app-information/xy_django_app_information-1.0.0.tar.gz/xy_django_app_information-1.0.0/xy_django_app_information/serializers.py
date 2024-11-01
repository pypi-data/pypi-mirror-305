# -*- coding: UTF-8 -*-


from .models import *
from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer


class SRegion(Serializer):
    default_value = ""

    class Meta:
        model = MRegion
        fields = "__all__"


class VSRegion(viewsets.ModelViewSet):
    queryset = MRegion.objects.all()
    serializer_class = SRegion


class SVersion(Serializer):
    default_value = ""

    class Meta:
        model = MVersion
        fields = "__all__"


class VSVersion(viewsets.ModelViewSet):
    queryset = MVersion.objects.all()
    serializer_class = SVersion


class SDevelopment(Serializer):
    default_value = ""

    class Meta:
        model = MVersion
        fields = "__all__"


class VSDevelopment(viewsets.ModelViewSet):
    queryset = MVersion.objects.all()
    serializer_class = SDevelopment


class SSystem(Serializer):
    default_value = ""

    class Meta:
        model = MSystem
        fields = "__all__"


class VSSystem(viewsets.ModelViewSet):
    queryset = MSystem.objects.all()
    serializer_class = SSystem


class SDevice(Serializer):
    default_value = ""

    class Meta:
        model = MDevice
        fields = "__all__"


class VSDevice(viewsets.ModelViewSet):
    queryset = MDevice.objects.all()
    serializer_class = SDevice
