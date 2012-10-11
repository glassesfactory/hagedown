#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from google.appengine.ext import db
from google.appengine.api import memcache

NUM_SHARDS = 20


class SystemInfoModel(db.Model):
    name = db.StringProperty()
    typeName = db.StringProperty()
    count = db.IntegerProperty(default=0)

    @classmethod
    def getArticleCount(cls):
        return cls()._getCount('article')

    @classmethod
    def incrementArticleCount(cls):
        return cls()._articleCount(1)

    @classmethod
    def decrementArticleCount(cls):
        return cls()._articleCount(-1)

    @classmethod
    def getTagCnt(cls, tagName):
        return cls()._getCount('tag', tagName)

    @classmethod
    def increamentTagCount(cls, tagName):
        cls()._tagCount(1, tagName=tagName)
        tags = SystemInfoModel.getAllTag()
        if tagName not in tags:
            tags.setdefault(tagName, 1)
        else:
            tags[tagName] += 1
        memcache.set('tagdict', tags)

    @classmethod
    def decrementTagCount(cls, tagName):
        return cls()._tagCount(-1, tagName=tagName)

    @classmethod
    def getAllTag(cls):
        tags = memcache.get('tagdict')
        if tags is not None:
            return tags
        else:
            models = cls().all().filter('typeName =', 'tag')
            tags = {}
            for tag in models:
                if tag.name not in tags:
                    tags.setdefault(tag.name, 1)
                else:
                    tags[tag.name] += 1
            memcache.set('tagdict', tags)
            return tags

    @classmethod
    def getAllTagList(cls, rev=True):
        tags = SystemInfoModel.getAllTag()
        return [{'name':k, 'count':v} for k, v in sorted(tags.items(), key=lambda x:x[1], reverse=rev)]

    def _getCount(self, typeName, tagName=None):
        total = 0
        counters = self.all().filter('typeName =', typeName)
        if typeName is 'tag':
            tags = SystemInfoModel.getAllTag()
            if tagName in tags:
                return tags[tagName]
            else:
                counters = counters.filter('name =', tagName)
        if counters.count() >= 1:
            for counter in counters:
                total += counter.count
            if typeName is 'tag':
                tags = SystemInfoModel().getAllTag()
                tags[tagName] = total
        return total

    def _articleCount(self, inc):
        def txn():
            index = random.randint(0, NUM_SHARDS - 1)
            shard_name = 'shard_art' + str(index)
            counter = SystemInfoModel.get_by_key_name(shard_name)
            if counter is None:
                counter = SystemInfoModel(key_name=shard_name)
                counter.typeName = 'article'
            counter.count += inc
            counter.put()
            return counter
        db.run_in_transaction(txn)

    def _tagCount(self, inc, tagName):
        def txn():
            index = random.randint(0, NUM_SHARDS - 1)
            shard_name = 'shard_tag' + str(index)
            counter = SystemInfoModel.get_by_key_name(shard_name)
            if counter is None:
                counter = SystemInfoModel(key_name=shard_name)
                counter.typeName = 'tag'
                counter.name = tagName
            counter.count += inc
            counter.put()
            return counter
        return db.run_in_transaction(txn)
