#!/usr/bin/env python
# -*- coding: utf-8 -*-

from formencode import validators as vs, Schema


class ArticleSchema(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    title = vs.UnicodeString(not_empty=True)
    text = vs.UnicodeString(not_empty=True)
    tags = vs.String()
