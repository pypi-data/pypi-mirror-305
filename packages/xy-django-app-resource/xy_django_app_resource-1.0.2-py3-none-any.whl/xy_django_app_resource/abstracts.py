# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "abstracts"
"""
  * @File    :   abstracts.py
  * @Time    :   2023/05/01 20:04:42
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.conf import settings

from xy_django_model.model import gen_upload_to


class MAPDFCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"),
        max_length=300,
        null=True,
        blank=True,
    )
    code = models.CharField(
        verbose_name=_("编码"),
        max_length=300,
        null=True,
        blank=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("PDF合集")
        verbose_name_plural = _("PDF合集")

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def pdfs(instance=None, filename=None):
    pass


class MAPDF(models.Model):
    id = models.BigAutoField(primary_key=True)

    pdf = models.FileField(verbose_name=_("PDF"), upload_to=pdfs, null=True, blank=True)
    url = models.URLField(verbose_name=_("图片链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("图片下载链接"), null=True, blank=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)

    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    def cdn_url_preview(self):
        return '<a href="{cdn_domain}/{path}" />'.format(
            cdn_domain=self.cdn_domain, path=self.path
        )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.pdf.url
        )

    icon_preview.short_description = _("图片")
    icon_preview.allow_tags = True

    cdn_url_preview.short_description = _("cdn地址")
    cdn_url_preview.allow_tags = True

    debug = True

    @property
    def pdf_url(self):
        protocol = "https"
        if self.debug == True:
            protocol = "http"
        if hasattr(settings, "PROTOCOL"):
            protocol = settings.PROTOCOL
        if self.pdf != None and bool(self.pdf):
            return protocol + "://" + settings.DOMAIN + self.pdf.url

        if self.cdn_domain != None and self.path != None:
            return "{cdn_domain}/{path}".format(
                cdn_domain=self.cdn_domain, path=self.path
            )

        if self.download_url != None:
            return self.download_url

        return self.url

    class Meta:
        abstract = True
        verbose_name = _("PDF")
        verbose_name_plural = _("PDF")

    def __str__(self):
        downloaded_text = ""
        if bool(self.pdf) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"


class MAImageCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("图片合集")
        verbose_name_plural = _("图片合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def images(instance=None, filename=None):
    pass


class MAImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(
        verbose_name=_("图片"), upload_to=images, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("图片链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("图片下载链接"), null=True, blank=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    def cdn_url_preview(self):
        return '<a href="{cdn_domain}/{path}" />'.format(
            cdn_domain=self.cdn_domain, path=self.path
        )

    def icon_preview(self):
        return '<img src="{image_url}" width="40px" height="40px" />'.format(
            image_url=self.image.url
        )

    icon_preview.short_description = _("图片")
    icon_preview.allow_tags = True

    cdn_url_preview.short_description = _("cdn地址")
    cdn_url_preview.allow_tags = True

    debug = True

    @property
    def image_url(self):
        protocol = "https"
        if self.debug == True:
            protocol = "http"
        if hasattr(settings, "PROTOCOL"):
            protocol = settings.PROTOCOL
        if self.image != None and bool(self.image):
            return protocol + "://" + settings.DOMAIN + self.image.url

        if self.cdn_domain != None and self.path != None:
            return "{cdn_domain}/{path}".format(
                cdn_domain=self.cdn_domain, path=self.path
            )

        if self.download_url != None:
            return self.download_url

        return self.url

    class Meta:
        abstract = True
        verbose_name = _("图片")
        verbose_name_plural = _("图片")
        app_label = "xy_django_app_resource"

    def __str__(self):
        downloaded_text = ""
        if bool(self.image) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"


class MAPackageCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )

    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("包合集")
        verbose_name_plural = _("包合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def packages(instance=None, filename=None):
    pass


class MAPackage(models.Model):
    id = models.BigAutoField(primary_key=True)

    package = models.FileField(
        verbose_name=_("包"), upload_to=packages, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("包链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("包下载链接"), null=True, blank=True, unique=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    def cdn_url_preview(self):
        return '<a href="{cdn_domain}/{path}" />'.format(
            cdn_domain=self.cdn_domain, path=self.path
        )

    cdn_url_preview.short_description = _("cdn地址")
    cdn_url_preview.allow_tags = True

    class Meta:
        abstract = True
        verbose_name = _("包")
        verbose_name_plural = _("包")
        app_label = "xy_django_app_resource"

    def __str__(self):
        downloaded_text = ""
        if bool(self.package) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"


@gen_upload_to
def bodies(instance=None, filename=None):
    pass


class MARequest(models.Model):
    id = models.BigAutoField(primary_key=True)

    url = models.URLField(verbose_name=_("请求链接"), null=True, blank=True)
    method = models.URLField(verbose_name=_("请求方法"), null=True, blank=True)
    body = models.FileField(
        verbose_name=_("Body"), upload_to=bodies, null=True, blank=True
    )
    body_text = models.TextField(verbose_name=_("Body_Text"), null=True, blank=True)
    cookie = models.TextField(verbose_name=_("Cookie"), null=True, blank=True)
    header = models.TextField(verbose_name=_("头部信息"), null=True, blank=True)
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    encoding = models.CharField(
        verbose_name=_("编码方式"), max_length=300, null=True, blank=True
    )
    priority = models.IntegerField(
        verbose_name=_("请求的优先级"), null=True, blank=True
    )
    # 默认为False，若设置为True，这次请求将不会过滤（不会加入到去重队列中），可以多次执行相同的请求
    dont_filter = models.BooleanField(verbose_name=_("重复请求"), null=True, blank=True)
    meta = models.TextField(verbose_name=_("meta"), null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = _("请求")
        verbose_name_plural = _("请求")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def responses(instance=None, filename=None):
    pass


class MAResponse(models.Model):
    id = models.BigAutoField(primary_key=True)

    url = models.URLField(verbose_name=_("响应链接"), null=True, blank=True)
    body = models.FileField(
        verbose_name=_("Body"), upload_to=responses, null=True, blank=True
    )
    body_text = models.TextField(verbose_name=_("Body_Text"), null=True, blank=True)
    headers = models.TextField(verbose_name=_("headers"), null=True, blank=True)
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )
    status_code = models.IntegerField(verbose_name=_("状态码"), null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = _("响应")
        verbose_name_plural = _("响应")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def html_files(instance=None, filename=None):
    pass


class MAHTMLFile(models.Model):
    id = models.BigAutoField(primary_key=True)

    html_file = models.FileField(
        verbose_name=_("HTML文件"), upload_to=html_files, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("HTML文件链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("HTML文件下载链接"), null=True, blank=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("HTML文件")
        verbose_name_plural = _("HTML文件")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


class MAVideoCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("视频合集")
        verbose_name_plural = _("视频合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def videos(instance=None, filename=None):
    pass


class MAVideo(models.Model):
    id = models.BigAutoField(primary_key=True)

    # 性别选择
    status_choices = (
        ("default", _("默认")),
        ("ready", _("就绪")),
        ("uploaded", _("已上传")),
    )

    video = models.FileField(
        verbose_name=_("视频"), upload_to=videos, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("视频链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("视频下载链接"), null=True, blank=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)

    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )
    duration = models.TimeField(verbose_name=_("时间长度"), null=True, blank=True)
    status = models.CharField(
        verbose_name=_("状态"),
        max_length=300,
        choices=status_choices,
        null=True,
        blank=True,
    )

    def cdn_url_preview(self):
        return '<a href="{cdn_domain}/{path}" />'.format(
            cdn_domain=self.cdn_domain, path=self.path
        )

    cdn_url_preview.short_description = _("cdn地址")
    cdn_url_preview.allow_tags = True
    debug = True

    @property
    def video_url(self):
        protocol = "https"
        if self.debug:
            protocol = "http"
        if hasattr(settings, "PROTOCOL"):
            protocol = settings.PROTOCOL
        if self.video != None:
            return protocol + "://" + settings.DOMAIN + self.video.url

        if self.cdn_domain != None and self.path != None:
            return "{cdn_domain}/{path}".format(
                cdn_domain=self.cdn_domain, path=self.path
            )

        if self.download_url != None:
            return self.download_url

        return self.url

    class Meta:
        abstract = True
        verbose_name = _("视频")
        verbose_name_plural = _("视频")
        app_label = "xy_django_app_resource"

    def __str__(self):
        downloaded_text = ""
        if bool(self.video) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"


class MAAudioCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("音频合集")
        verbose_name_plural = _("音频合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def audios(instance=None, filename=None):
    pass


class MAAudio(models.Model):
    id = models.BigAutoField(primary_key=True)

    audio = models.FileField(
        verbose_name=_("音频"), upload_to=audios, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("音频链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("音频下载链接"), null=True, blank=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)
    duration = models.TimeField(verbose_name=_("时间长度"), null=True, blank=True)

    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    debug = True

    @property
    def audio_url(self):
        protocol = "https"
        if self.debug:
            protocol = "http"
        if hasattr(settings, "PROTOCOL"):
            protocol = settings.PROTOCOL
        if self.audio != None:
            return protocol + "://" + settings.DOMAIN + self.audio.url

        if self.cdn_domain != None and self.path != None:
            return "{cdn_domain}/{path}".format(
                cdn_domain=self.cdn_domain, path=self.path
            )

        if self.download_url != None:
            return self.download_url

        return self.url

    class Meta:
        abstract = True
        verbose_name = _("音频")
        verbose_name_plural = _("音频")
        app_label = "xy_django_app_resource"

    def __str__(self):
        downloaded_text = ""
        if bool(self.audio) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"


class MATextCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _("文本合集")
        verbose_name_plural = _("文本合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


class MAText(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(verbose_name=_("文本"), null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = _("文本")
        verbose_name_plural = _("文本")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


class MAFileCollection(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    code = models.CharField(
        verbose_name=_("编码"), max_length=300, null=True, blank=True
    )

    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    class Meta:
        abstract = True
        verbose_name = _("文件合集")
        verbose_name_plural = _("文件合集")
        app_label = "xy_django_app_resource"

    def __str__(self):
        return f"{self.id}. {self.name}"


@gen_upload_to
def files(instance=None, filename=None):
    pass


class MAFile(models.Model):
    id = models.BigAutoField(primary_key=True)

    file = models.FileField(
        verbose_name=_("文件"), upload_to=files, null=True, blank=True
    )
    url = models.URLField(verbose_name=_("文件链接"), null=True, blank=True)
    download_url = models.URLField(
        verbose_name=_("文件下载链接"), null=True, blank=True, unique=True
    )
    name = models.CharField(
        verbose_name=_("名称"), max_length=300, null=True, blank=True
    )
    width = models.FloatField(verbose_name=_("宽度"), null=True, blank=True)
    height = models.FloatField(verbose_name=_("高度"), null=True, blank=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"), null=True, blank=True, auto_now_add=True
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"), null=True, blank=True, auto_now_add=True
    )
    description = models.TextField(verbose_name=_("简介"), null=True, blank=True)
    path = models.CharField(
        verbose_name=_("路径"), max_length=300, null=True, blank=True
    )
    cdn_domain = models.CharField(
        verbose_name=_("CDN域名"), max_length=300, null=True, blank=True
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        null=True,
        blank=True,
        default=uuid.uuid4,
        editable=True,
        unique=True,
    )

    def cdn_url_preview(self):
        return '<a href="{cdn_domain}/{path}" />'.format(
            cdn_domain=self.cdn_domain, path=self.path
        )

    cdn_url_preview.short_description = _("cdn地址")
    cdn_url_preview.allow_tags = True

    class Meta:
        abstract = True
        verbose_name = _("文件")
        verbose_name_plural = _("文件")
        app_label = "xy_django_app_resource"

    def __str__(self):
        downloaded_text = ""
        if bool(self.file) == True:
            downloaded_text = " [已下载]"
        return f"{self.id}. {self.name}{downloaded_text}"
