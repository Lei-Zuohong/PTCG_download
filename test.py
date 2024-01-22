# -*- coding: UTF-8 -*-
# Public package
# Private package
# Internal package
import re
import os
import wget
import numpy
import urllib.request
import multiprocessing

path = 'https://limitlesstcg.com/cards'
html = urllib.request.urlopen(path).read().decode('utf-8')
allcheck = re.findall(r'<a href="/cards/([A-Z]*)">[0-9][0-9]', html)
allcheck = numpy.unique(allcheck)
for check in allcheck:
    path_card = '%s/%s' % (path, check)
    html_card = urllib.request.urlopen(path_card).read().decode('utf-8')
    allcheck_card = re.findall(r'src="https://limitlesstcg.nyc3.digitaloceanspaces.com/tpci/(.*)/(.*).png', html_card)
    os.makedirs('card/%s' % (check), exist_ok=True)
    for check_card in allcheck_card:
        print(check_card[1][:-3])
        wget.download('https://limitlesstcg.nyc3.digitaloceanspaces.com/tpci/%s/%s.png' % (check_card[0], check_card[1][:-3]), 'card/%s/%s.png' % (check_card[0], check_card[1][:-3]))


# html = urllib.request.urlopen(path).read()
# allcheck = re.findall(r'src="https://limitlesstcg.nyc3.digitaloceanspaces.com/tpci/(.*)/(.*).png', html.decode('utf-8'))
# for check in allcheck


# <a href="/cards/PAL">