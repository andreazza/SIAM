# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:45:38 2020

@author: carlo
"""

import re

text = "asdfasdf Alteração realizada com êxito. asfasd"
regex = re.compile(f'(\w+)(\s*)êxito')
result = regex.search(text)
result.group(1)
