#!/usr/bin/env python
#imports modules

import os
import shutil
import time
import sched
from PIL import Image

#Taking user input
idir=input("Enter the directory of Wallpapers")
#defines the directory of location of running Script
dst=os.path.dirname(os.path.abspath(__file__))

#copies all files from user's directory to dst
for i in os.listdir(idir):
    shutil.copy(idir,dst)

#extracts files of .jpg ang .jpeg extension and opens it
for j in os.listdir(idir):
    fname,ext = os.path.splitext(j)
    if ext==".jpg" or ext==".jpeg" :
        im=Image.OPEN(idir)
