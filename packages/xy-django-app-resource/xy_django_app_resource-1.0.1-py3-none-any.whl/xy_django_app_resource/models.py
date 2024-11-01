# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from .abstracts import *


class MPDFCollection(MAPDFCollection):
    pdfs = models.ManyToManyField(
        "xy_django_app_resource.MPDF",
        verbose_name=_("PDF"),
        related_name="%(app_label)s_%(class)s_pdfs",
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MPDF(MAPDF):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MImageCollection(MAImageCollection):
    images = models.ManyToManyField(
        "xy_django_app_resource.MImage",
        verbose_name=_("图片"),
        related_name="%(app_label)s_%(class)s_images",
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MImage(MAImage):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_region",
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MPackageCollection(MAPackageCollection):
    packages = models.ManyToManyField(
        "xy_django_app_resource.MPackage",
        verbose_name=_("包"),
        related_name="%(app_label)s_%(class)s_packages",
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MPackage(MAPackage):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MRequest(MARequest):
    response = models.OneToOneField(
        "xy_django_app_resource.MResponse",
        verbose_name=_("响应"),
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_response",
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MResponse(MAResponse):
    class Meta:
        app_label = "xy_django_app_resource"


class MHTMLFile(MAHTMLFile):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_region",
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MVideoCollection(MAVideoCollection):
    videos = models.ManyToManyField(
        "xy_django_app_resource.MVideo",
        verbose_name=_("视频"),
        related_name="%(app_label)s_%(class)s_videos",
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MVideo(MAVideo):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_region",
        null=True,
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MAudioCollection(MAAudioCollection):
    audios = models.ManyToManyField(
        "xy_django_app_resource.MAudio",
        verbose_name=_("音频"),
        related_name="%(app_label)s_%(class)s_audios",
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MAudio(MAAudio):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("包")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MTextCollection(MATextCollection):
    texts = models.ManyToManyField(
        "xy_django_app_resource.MText",
        verbose_name=_("文本"),
        related_name="%(app_label)s_%(class)s_texts",
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_resource"


class MText(MAText):
    class Meta:
        app_label = "xy_django_app_resource"


class MFileCollection(MAFileCollection):
    files = models.ManyToManyField(
        "xy_django_app_resource.MFile",
        verbose_name=_("文件"),
        related_name="%(app_label)s_%(class)s_files",
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("文件")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"


class MFile(MAFile):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("位置"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cover = models.ForeignKey(
        "xy_django_app_resource.MImage",
        verbose_name=_("封面"),
        related_name="%(app_label)s_%(class)s_cover",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.cover.image_url
        )

    icon_preview.short_description = _("文件")
    icon_preview.allow_tags = True

    class Meta:
        app_label = "xy_django_app_resource"
