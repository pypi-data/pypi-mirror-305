# -*- coding: UTF-8 -*-


from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MApiAuthCredential)
class AApiAuthCredential(admin.ModelAdmin):
    pass


@admin.register(MApiAuthCredentialCache)
class AApiAuthCredentialCache(admin.ModelAdmin):
    pass
