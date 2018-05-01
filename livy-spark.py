#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, pprint, requests, textwrap

# 建立session
host = 'http://10.0.3.50:8998'
headers = {'Content-Type': 'application/json'}

session_url = host + '/sessions/5'
statements_url = session_url + '/statements'
# 传输代码片段
data = {
    'code': textwrap.dedent("""
    val NUM_SAMPLES = 100000;
    val count = sc.parallelize(1 to NUM_SAMPLES).map { i =>
      val x = Math.random();
      val y = Math.random();
      if (x*x + y*y < 1) 1 else 0
    }.reduce(_ + _);
    println(\"Pi is roughly \" + 4.0 * count / NUM_SAMPLES)
    """)
}

r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())

