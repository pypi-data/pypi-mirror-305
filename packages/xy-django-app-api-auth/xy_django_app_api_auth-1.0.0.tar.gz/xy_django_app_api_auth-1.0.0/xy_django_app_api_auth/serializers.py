# -*- coding: UTF-8 -*-


from .models import *
from rest_framework import viewsets
from xy_django_serializer.Serializer import Serializer


class SApiAuthCredential(Serializer):

    default_value = ""

    class Meta:
        model = MApiAuthCredential
        fields = "__all__"


# ViewSets define the view behavior.
class VSApiAuthCredential(viewsets.ModelViewSet):
    queryset = MApiAuthCredential.objects.all()
    serializer_class = SApiAuthCredential


# Serializers define the API representation.
class SApiAuthCredentialCache(Serializer):

    default_value = ""

    class Meta:
        model = MApiAuthCredentialCache
        fields = "__all__"


# ViewSets define the view behavior.
class VSApiAuthCredentialCache(viewsets.ModelViewSet):
    queryset = MApiAuthCredentialCache.objects.all()
    serializer_class = SApiAuthCredentialCache
