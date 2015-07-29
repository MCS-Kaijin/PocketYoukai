# coding: utf-8

import urllib
import zipfile
import os

filename, headers = urllib.urlretrieve('https://codeload.github.com/MCS-Kaijin/PocketYoukai/zip/master')

with zipfile.ZipFile(filename) as f:
	f.extractall()
with open('PocketYoukai-master/main.py','r') as nc:
	with open('main.py','w') as oc:
		oc.truncate()
		oc.write(nc.read())

for file in os.listdir('PocketYoukai-master'):
	os.remove('PocketYoukai-master/'+file)
os.removedirs('PocketYoukai-master')
