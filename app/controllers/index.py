#!/usr/bin/env python
# -*- coding: utf-8 -*-

from formencode import htmlfill

from shimehari import request, ApplicationController, redirect, flash, getFlashedMessage
from shimehari.configuration import ConfigManager

from app.models.articles import ArticleModel
from app.models.sites import SystemInfoModel
from app.models.tags import createTags, updateTags
from app.helpers.paginator import Pagination

PER_PAGE = ConfigManager.getConfig()['PER_PAGE']


class IndexController(ApplicationController):
    def __init__(self, name):
        ApplicationController.__init__(self, name)

    def index(self, *args, **kwargs):
        u"""メモを一覧で表示します。"""
        page = kwargs['page'] if 'page' in kwargs else 1
        count = SystemInfoModel.getArticleCount()
        articles = ArticleModel.getArticleForPage(page, PER_PAGE)
        pagination = Pagination(page, PER_PAGE, count)
        alert = dict(getFlashedMessage(withCategory=True))
        return self.renderTemplate('index/index.html', articles=articles, pagination=pagination, pagePath='/page/', alert=alert)

    def show(self, *args, **kwargs):
        u"""メモの詳細を表示します。"""
        id = kwargs['id']
        model = ArticleModel.get_by_id(id)
        article = ArticleModel.getArticle(model)
        alert = dict(getFlashedMessage(withCategory=True))
        return self.renderTemplate('index/show.html', article=article, alert=alert)

    def edit(self, *args, **kwargs):
        u"""メモを編集します。"""
        alert = dict(getFlashedMessage(withCategory=True))
        id = kwargs['id']
        model = ArticleModel.get_by_id(id)
        form = self.renderTemplate('index/form.html', action='/' + str(id), method='PUT')
        defaults = {
            'title': model.title,
            'text': model.text,
            'tags': ','.join([tag.tagname for tag in model.tags])
        }
        form = htmlfill.render(form, defaults)
        return self.renderTemplate('index/edit.html', form=form, alert=alert)

    def new(self, *args, **kwargs):
        u"""メモの新規作成画面を表示します。"""
        form = self.renderTemplate('index/form.html', action='/', method='POST')
        return self.renderTemplate('index/new.html', form=form)

    def create(self, *args, **kwargs):
        u"""メモの新規保存処理をします。"""
        form = request.form.copy()
        result, data = ArticleModel.validate(form)
        if not result:
            alert = {'errors': data}
            tmp = self.renderTemplate('index/form.html', action="/", method="POST")
            defaults = {
                'title': form['title'],
                'text': form['text'],
                'tags': form['tags']
            }
            form = htmlfill.render(tmp, defaults)
            return self.renderTemplate('index/new.html', form=form, alert=alert)
        else:
            model = ArticleModel()
        try:
            model.publish(title=data['title'], text=data['text'])
            SystemInfoModel.incrementArticleCount()
            createTags(data['tags'], model)
            flash(u'保存したかもしれない', 'success')
        except:
            flash((u'失敗したぽよ'), 'errors')
        return redirect('/')

    def update(self, *args, **kwargs):
        u"""メモの編集結果を保存します。"""
        form = request.form.copy()
        id = kwargs['id']
        try:
            model = ArticleModel.get_by_id(id)
            model.publish(title=form['title'], text=form['text'])
            updateTags(form['tags'], model)
            flash(u'保存したと思います。', 'success')
        except:
            flash((u'失敗しますた…'), 'errors')
        return '/' + str(id)

    def destroy(self, *args, **kwargs):
        u"""メモを破棄します。"""
        id = kwargs['id']
        try:
            ArticleModel.deleteModel(id)
            SystemInfoModel.decrementArticleCount()
            flash(u'次はお前がこうなる番だ…','success')
        except:
            flash((u'失敗したよ'),'errors')
        return '/'
