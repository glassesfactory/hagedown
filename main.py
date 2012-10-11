#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shimehari import Shimehari, shared
import config
from app.models.sites import SystemInfoModel

app = Shimehari(__name__)


@app.beforeRequest
def testReq():
    tagList = SystemInfoModel.getAllTagList()[:5]
    shared.tagList = tagList


if __name__ == '__main__':
    app.drink()
