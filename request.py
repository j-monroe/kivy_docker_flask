#!/usr/bin/python
import requests 
r = requests.get('http://198.199.110.182:8080')
print(r.status_code)
