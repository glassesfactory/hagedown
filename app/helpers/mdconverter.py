#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import markdown

ptn = re.compile(r'\n|\r')


def convertMarkdown(md):
    return markdown.markdown(md)


def lineSlicer(headline, length=3):
    i = 0
    cursor = 0
    while i < length:
        m = ptn.search(headline, cursor)
        if m is not None:
            cursor = m.end() + 1
            i += 1
        else:
            break
    if cursor == 0:
        cursor = len(headline)
    return cursor
