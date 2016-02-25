#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: detailyang
# @Date:   2016-02-25 11:23:59
# @Last Modified by:   detailyang
# @Last Modified time: 2016-02-25 12:47:01

import re
import sys
from requests import get

url_re = re.compile('.*\((.*?)\)')

for i in range(ord('a'), ord('z')+1):
    file = 'docs/{alphabet}.md'.format(alphabet=chr(i))
    with open(file) as f:
        for line, content in enumerate(f.readlines()):
            m = re.match(url_re, content)
            if m is None:
                continue
            result = get(m.group(1))
            if result.status_code >= 400:
                print('{file} line #{line} {url} return {code}'.format(file=file, line=line,
                    url=m.group(1), code=result.status_code))
                sys.exit(1)