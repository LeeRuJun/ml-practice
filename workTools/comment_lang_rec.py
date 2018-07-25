#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import langid

# langid.set_languages(['en', 'zh'])

for line in sys.stdin:
    if line == "":
        break
    line = line.strip()
    if '\t' in line:
        commentId, content = line.split('\t', 1)
        langType = langid.classify(content)
        if langType:
            print '\t'.join([commentId, langType[0]])

