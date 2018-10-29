#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

link = "http://"+input("Url giriniz...\nSite :")

paneller = []
if (link[len(link)-1:] != '/'):
    link = link + '/'

wordlist = open("/home/fkarababa/Desktop/wordlist.txt", "r")
for i in wordlist:
    deneme = link + i
    response = requests.get(deneme)
    if(response.status_code == 200):
        print("Panel = {}\n".format(deneme))
        paneller.append(deneme)

if (len(paneller) == 0):
    print("Admin paneli bulunmadı ...")
elif (len(paneller) > 0):
    print(paneller)
