#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shimehari import ApplicationController
from shimehari.configuration import ConfigManager

from app.models.articles import ArticleModel
from app.models.sites import SystemInfoModel
from app.models.tags import TagModel
from app.helpers.paginator import Pagination

PER_PAGE = ConfigManager.getConfig()['PER_PAGE']


class TagsController(ApplicationController):
    def __init__(self, name):
        ApplicationController.__init__(self, name)

    def index(self, *args, **kwargs):
        tags = SystemInfoModel.getAllTagList()
        tagList = []
        for tag in tags:
            if tag['count'] > 12:
                tag['size'] = 12
            else:
                tag['size'] = tag['count']
            tagList.append(tag)
        return self.renderTemplate('tags/index.html', tagList=tagList)

    def tagIndex(self, *args, **kwargs):
        name = kwargs['tagname']
        page = kwargs['page'] if 'page' in kwargs else 1
        count = SystemInfoModel.getTagCnt(name)
        start = (page - 1) * PER_PAGE
        models = TagModel.all().filter('tagname =', name).order('-created_at').fetch(PER_PAGE, start)
        pagination = Pagination(page, PER_PAGE, count)
        articles = [ArticleModel.getArticle(m.article) for m in models]
        pagePath = '/tags/' + name + '/page/'
        return self.renderTemplate('index/index.html', articles=articles, pagination=pagination, tagname=name, pagePath=pagePath)
