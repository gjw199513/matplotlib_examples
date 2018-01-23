# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/23 0023 下午 2:31'

import json
from urllib.parse import urlparse
from os.path import basename, join, exists
from os import renames

DOWNLOAD_DIR = 'downloads'
with open('res2.json') as f:
    for item in json.load(f):
        for df in item['files']:
            src = join(DOWNLOAD_DIR, df['path'])
            # 将文件夹+分类信息+基本文件名 连接
            dst = join(DOWNLOAD_DIR, item['section'], basename(urlparse(df['url']).path))
            if exists(src):
                print(src, dst)
                renames(src, dst)
