#!/usr/bin/python3

"""
Downloads community profiles from https://github.com/freifunk/openwrt-packages.git
As github does not support git-archive, we can accomplish that task only via svn (which would
add up another dependency for the build system and might not be avaiable at all hosts by default)
or this script, which gets the download-links from github api and downloads them individually.

This script was inspired by this stackoverflow-post:
https://stackoverflow.com/a/59100287
"""

import requests
import time
import sys
#import json

#where to store the profiles
syspath = sys.argv[1]
path = syspath + "/files/etc/config/"
# api-call for the folder containing the profiles. Gives a json.
folder_url = "https://api.github.com/repos/freifunk/openwrt-packages/contents/contrib/package/community-profiles/files/etc/config?ref=master"
files_json = requests.get(folder_url).json()
#with open("files.json", "w") as g:
#	g.write(json.dumps(files_json))

time.sleep(5)

for file in files_json:
	name = file.get("name")
	url = file.get("download_url")
	content = requests.get(url)
	with open(path+name, "w") as f:
		f.write(content.text)
	time.sleep(3)
