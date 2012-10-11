#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shimehari import Router, Resource
from controllers import IndexController, TagsController


index = IndexController('index')
tags = TagsController('tags')

appRoutes = Router([
    #GAE だと DELETE メソッドが使えんのね…
    Resource(index, root=True).addRule('/page/<int:page>', index.index, methods=['GET']).addRule('/del/<int:id>', index.destroy, methods=['POST']),
    Resource(tags).addRule('/tags/<tagname>', tags.tagIndex, methods=['GET']).addRule('/tags/<tagname>/page/<int:page>', tags.tagIndex, methods=['GET'])
])
