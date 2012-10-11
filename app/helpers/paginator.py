#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil


class Pagination(object):
    def __init__(self, page, perPage, count):
        self.page = page
        self.perPage = perPage
        self.count = count

    @property
    def pages(self):
        return int(ceil(self.count / float(self.perPage)))

    @property
    def hasPrev(self):
        return self.page > 1

    @property
    def hasNext(self):
        return self.page < self.pages

    def iterPages(self, leftEdge=2, leftCurrent=2, rightCurrent=5, rightEdge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= leftEdge or \
                (num > self.page - leftCurrent - 1 and num < self.page + rightCurrent) or \
                num > self.pages - rightEdge:
                    if last + 1 != num:
                        yield None
                    yield num
                    last = num
