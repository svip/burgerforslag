#!/usr/bin/env python3

import urllib.request
import json
import time

def infrange():
    i = 0
    while True:
        yield i
        i += 1

ids = []
for i in infrange():
    req = urllib.request.Request(
        'https://www.borgerforslag.dk/api/proposals/search',
        data=json.dumps({'filter': 'all', 'sortOrder': 'latest',
                         'searchQuery': '', 'pageNumber': str(i),
                         'pageSize': '100'}).encode('utf-8'),
        headers={'Content-Type': 'text/json'})
    with urllib.request.urlopen(req) as f:
        res = json.loads(f.read().decode('utf-8'))
    if len(res['data']) == 0:
        break
    for d in res['data']:
        ids.append(d['externalId'].split('-')[1])
    time.sleep(1)
ids.sort()
print('\n'.join(ids))
