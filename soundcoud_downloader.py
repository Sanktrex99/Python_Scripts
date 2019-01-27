#!/usr/bin/env python
#import modules
import sys
import re
import urllib2
import requests

#User's Input
cli_id = input("Enter your Client ID!")
track_url = input("Enter the URL of the track to be downloaded!!")
json_stream = requests.get(track_url)

song_url = input("Enter the song's URL!")
a = re.match(r'^https*://(www.)*soundcloud\.com/',song_url)

#requesting from the URL
html = requests.get(song_url)
title = re.search('<title>([^|]+) | Free Listening on SoundCloud</title>',html.text, re.IGNORECASE)
song_id = re.search(r'soundcloud://sounds:(\d+)', html.text, re.IGNORECASE)

song_url = input("Enter the song's URL!")
a = re.match(r'^https*://(www.)*soundcloud\.com/',song_url)
song_id= re.search(r'soundcloud://sounds:(\d+)', html.text, re.IGNORECASE)

#Downloading the Audio in Mp3 format
f = urllib2.urlopen(json_stream.json()['http_mp3_128_url'])
with open("{0}.mp3".format(title), "wb") as song:
    song.write(f.read())
