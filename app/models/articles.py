#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from formencode import Invalid
from shimehari.helpers import Stripper

from google.appengine.ext import db
from app.helpers.mdconverter import convertMarkdown, lineSlicer
from app.helpers.validator import ArticleSchema

stripper = Stripper()


class ArticleModel(db.Model):
    title = db.StringProperty()
    text = db.StringProperty(multiline=True)
    created_at = db.DateTimeProperty(auto_now_add=True)

    def publish(self, title, text):
        self.title = title
        self.text = text
        self.put()
        return self

    def getTime(self):
        return (self.created_at + datetime.timedelta(hours=9)).strftime('%Y/%m/%d %H:%M')

    @classmethod
    def validate(cls, form):
        schema = ArticleSchema()
        try:
            params = schema.to_python(form)
            params['text'] = stripper.strip(params['text'])
        except Invalid, e:
            errors = e.error_dict
            return False, errors
        return True, params

    @classmethod
    def getArticleForPage(cls, page, perPage):
        start = (page - 1) * perPage
        models = cls.all().order('-created_at').fetch(perPage, offset=start)
        articles = []
        if models is not None:
            for m in models:
                article = ArticleModel.getArticle(m)
                articles.append(article)
        return articles

    @classmethod
    def getArticle(self, model):
        article = {}
        article['id'] = model.key().id()
        article['title'] = model.title
        article['text'] = convertMarkdown(model.text)
        article['created_at'] = model.getTime()
        article['tags'] = [tag.tagname for tag in model.tags]
        article['pre'] = model.text[:lineSlicer(model.text)]
        if len(article['tags']) == 1 and article['tags'][0] == '':
            article['tags'] = []
        return article

    @classmethod
    def deleteModel(cls, id):
        model = ArticleModel.get_by_id(id)
        if model.tags is not None:
            for tag in model.tags:
                tag.deleteModel()
        model.delete()
