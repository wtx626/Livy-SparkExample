#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

headers = {'Content-Type': 'application/json'}
# 关闭session
session_url = 'http://10.0.3.50:8998/sessions/5'
requests.delete(session_url, headers=headers)
