#!/usr/bin/env python
#-*-coding:utf-8-*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^qtype$', views.question_type, name="qtype"),
    url(r'^qdiff$', views.question_difficult, name="qdiff"),
    url(r'^qkg$', views.question_knowledge, name="qkg"),
    url(r'^qkgp$', views.question_knowledge_post, name="qkgp"),
    url(r'^qcreate$', views.question_create, name="qcreate"),
    url(r'^qcreate$', views.question_create, name="qcreate"),
    url(r'^qlist$', views.question_list, name="qlist"),
    url(r'^atzujuan$', views.auto_zujuan, name="atzujuan"),
    url(r'^qdetail/(?P<qid>\w+)$', views.question_detail, name="qdetail"),
    url(r'^qedit/(?P<qid>\w+)$', views.question_edit, name="qedit"),
    url(r'^delete/q/(?P<qid>\w+)$', views.question_delete, name="qdelete"),
]
