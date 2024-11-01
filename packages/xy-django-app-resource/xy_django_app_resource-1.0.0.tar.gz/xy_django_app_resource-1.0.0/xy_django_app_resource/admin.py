# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *


@admin.register(MPDFCollection)
class APDFCollection(admin.ModelAdmin):
    filter_horizontal = [
        "pdfs",
    ]


@admin.register(MPDF)
class APDF(admin.ModelAdmin):
    pass


@admin.register(MImageCollection)
class AImageCollection(admin.ModelAdmin):
    filter_horizontal = [
        "images",
    ]


@admin.register(MImage)
class AImage(admin.ModelAdmin):
    list_display = (
        "identifier",
        "id",
        "name",
    )
    readonly_fields = ("icon_preview",)
    search_fields = ["id", "name", "identifier"]


@admin.register(MPackageCollection)
class APackageCollection(admin.ModelAdmin):
    filter_horizontal = [
        "packages",
    ]


@admin.register(MPackage)
class APackage(admin.ModelAdmin):
    pass


@admin.register(MRequest)
class ARequest(admin.ModelAdmin):
    pass


@admin.register(MResponse)
class AResponse(admin.ModelAdmin):
    pass


@admin.register(MHTMLFile)
class AHTMLFile(admin.ModelAdmin):
    pass


@admin.register(MVideoCollection)
class AVideoCollection(admin.ModelAdmin):
    filter_horizontal = [
        "videos",
    ]


@admin.register(MVideo)
class AVideo(admin.ModelAdmin):
    pass


@admin.register(MAudioCollection)
class AudioCollection(admin.ModelAdmin):
    filter_horizontal = [
        "audios",
    ]


@admin.register(MAudio)
class Audio(admin.ModelAdmin):
    pass


@admin.register(MTextCollection)
class TextCollection(admin.ModelAdmin):
    filter_horizontal = [
        "texts",
    ]


@admin.register(MText)
class Text(admin.ModelAdmin):
    pass
