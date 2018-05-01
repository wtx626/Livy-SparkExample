#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, pprint, requests

# 建立session
host = 'http://10.0.3.50:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
session_url = host + r.headers['location']
print(session_url)
