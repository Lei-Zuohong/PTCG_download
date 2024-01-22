# -*- coding: UTF-8 -*-
# Public package
import os
import time
import tqdm
import wget
# Private package
import headpy.hfile as hfile
# Internal package

packs = hfile.pkl_read('2.card_name.pkl')
for pack in packs:
    os.makedirs('card/%s' % (pack), exist_ok=True)
    bar = tqdm.tqdm(total=len(packs[pack]))
    for card in packs[pack]:
        check = 0
        if (os.path.isfile('card/%s/%s.png' % (card[0], card[1]))):
            bar.update(1)
            continue
        while (check < 5):
            try:
                url = 'https://limitlesstcg.nyc3.digitaloceanspaces.com/tpci/%s/%s.png' % (card[0], card[1])
                wget.download(url, 'card/%s/%s.png' % (card[0], card[1]))
                bar.update(1)
                check = 5
                time.sleep(2)
            except BaseException:
                check += 1
                time.sleep(2)
