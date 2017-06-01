#!/usr/bin/env python
#-*-coding:utf-8-*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('zujuan.urls')),
    url(r'^zujuan/', include('zujuan.urls', namespace='zujuan')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
