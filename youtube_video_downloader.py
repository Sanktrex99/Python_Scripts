#!/usr/bin/env python
#imports modules
import pafy
import time
from pytube import Youtube

time.sleep(2)
#Taking user input
url=input("Enter the link of the Youtube to be Downloaded!!!")
time.sleep(3)
dir=input("Enter the location of download!!!")
video=pafy.new(url)

print("Now Downloading /n in best resolution /n .........")

time.sleep(2)
#Prints video details as given
print(video.title," by:- ",video.author,"of duration",video.duration)
time.sleep(2)
print("Likes:-",video.likes,  "    Dislikes:-",video.dislikes)
print("Description:-",video.description)

try:
    sd=Youtube(url)
except:
    print("Error in Connecting ")

#filters only mp4 file
mp4files=sd.filter('mp4')
sd.set_filename("video.title")

d_video = sd.get(mp4files[-1].extension,mp4files[-1].resolution)
try:

    d_video.download(dir)
except:
    print("Some Error!")
print('Task Completed!')
