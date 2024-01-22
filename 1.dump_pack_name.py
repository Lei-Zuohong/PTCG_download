# -*- coding: UTF-8 -*-
# Public package
import re
import numpy
# Private package
import headpy.hfile as hfile
# Internal package
import urllib.request

path = 'https://limitlesstcg.com/cards'
html = urllib.request.urlopen(path).read().decode('utf-8')
allcheck = re.findall(r'<a href="/cards/([A-Z]*)">[0-9][0-9]', html)
allcheck = numpy.unique(allcheck).tolist()
hfile.pkl_dump('1.pack_name.pkl', allcheck)


