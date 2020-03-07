#! /usr/bin/env pythonpip install requestspip install requests
# -*- coding: utf-8 -*-

import requests
import json

lang_to = 'ja'
key = ""
file_to_translate = 'test.po'


def do_translation(text):
    if text == '':
        return ''
    try:

        url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}".format(key, text, lang_to)
        r = requests.get(url)
        res = json.loads(r.text)['text'][0]
        return res
    except:
        return ''


with open(file_to_translate, 'r', encoding='utf-8') as _file:
    data = _file.read().split('\n')

keys = []

for d in data:
   
    if 'msgid ' in d:   
        keys.append(d.replace('msgid ', '').replace('"', ''))
        
for k in keys:
    try:
        if k != '':
            res = do_translation(k)

            print('msgid "{}"'.format(k))
            print('msgstr "{}"'.format(res))
            print ('')
    except:
        pass
