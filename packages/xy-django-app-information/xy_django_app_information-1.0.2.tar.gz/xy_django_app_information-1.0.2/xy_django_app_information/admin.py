# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    search_fields = [
        "id",
        "name",
        "country",
        "province",
        "city",
        "district",
        "town",
        "address",
    ]


@admin.register(MVersion)
class AVersion(admin.ModelAdmin):
    filter_horizontal = [
        "versions",
    ]


@admin.register(MDevelopment)
class ADevelopment(admin.ModelAdmin):
    pass


@admin.register(MSystem)
class ASystem(admin.ModelAdmin):
    pass


@admin.register(MDevice)
class ADevice(admin.ModelAdmin):
    pass
