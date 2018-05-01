#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests, pprint

host = 'http://10.0.3.50:8998'
headers = {'Content-Type': 'application/json'}
statement_url = host + '/sessions/5/statements/0'
r = requests.get(statement_url, headers=headers)
pprint.pprint(r.json())
