# -*- coding: UTF-8 -*-
# Public package
import re
import time
import tqdm
import numpy
import multiprocessing
import urllib.request
# Private package
import headpy.hfile as hfile
# Internal package


def dump_card(pack):
    path_card = 'https://limitlesstcg.com/cards/%s' % (pack)
    html_card = urllib.request.urlopen(path_card).read().decode('utf-8')
    allcheck = re.findall(r'src="https://limitlesstcg.nyc3.digitaloceanspaces.com/tpci/(.*)/(.*).png', html_card)
    output = [[check[0], check[1][:-3]] for check in allcheck]
    return output


if __name__ == '__main__':
    packs = hfile.pkl_read('1.pack_name.pkl')
    pool = multiprocessing.Pool(processes=1)
    output = {}
    bar = tqdm.tqdm(total=len(packs))
    for pack in packs:
        check = False
        while (not check):
            try:
                output[pack] = dump_card(pack)
                bar.update(1)
                check = True
                time.sleep(5)
            except:
                time.sleep(5)
    hfile.pkl_dump('2.card_name.pkl', output)
