#! /usr/bin/env python3

import os
import requests

dir="/data/feedback/"
url= "http://35.238.38.53/feedback/" 
# url= "{your own corpweb external IP address}/feedback/"

for file in os.listdir(dir):
    fieldnames = ["title","name","date","feedback"]
    content = {}
    print(file)
    with open(dir+"/"+file, "r") as txtfile:
       x = 0
       for line in txtfile:
           content[fieldnames[x]] = line.rstrip('\n')
           x += 1
    print(content)

    response = requests.post(url,json=content)
    