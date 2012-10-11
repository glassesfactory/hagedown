#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db
from shimehari.logging import createLogger
from app.models.articles import ArticleModel
from app.models.sites import SystemInfoModel

logger = createLogger()


class TagModel(db.Model):
    tagname = db.StringProperty()
    article = db.ReferenceProperty(ArticleModel, collection_name='tags')
    created_at = db.DateTimeProperty(auto_now_add=True)

    def publish(self, name, article):
        self.tagname = name
        self.article = article
        self.put()
        return self

    def deleteModel(self):
        SystemInfoModel.decrementTagCount(self.tagname)
        self.delete()


def createTags(tags, article):
    tagList = tags.split(',')
    results = []
    for tag in tagList:
        m = TagModel()
        m.publish(tag, article)
        SystemInfoModel.increamentTagCount(tag)
        results.append(str(m.tagname))
    return results


def updateTags(tags, article):
    tagList = tags.split(',')
    olds = article.tags
    tagNames = [tag.tagname for tag in olds]
    results = []
    out = []
    for tag in olds:
        if tag.tagname not in tagList:
            out.append(tag)
    for tag in tagList:
        if tag not in tagNames:
            m = TagModel()
            m.publish(tag, article)
            SystemInfoModel.increamentTagCount(tag)
        results.append(tag)
    #
    db.delete(out)
    for tag in out:
        SystemInfoModel.decrementTagCount(tag.tagname)
    return results