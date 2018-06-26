#!/usr/bin/python


import os
from glob import glob
import subprocess


for fileName in glob("*.mp3"):
    dashPos = fileName.find(" - ")
    if dashPos != -1:
        artist = fileName[:dashPos]
        title = fileName[dashPos+3:-4]
        args = ["id3v2", "--artist", " \"" + artist + "\" ", "--song", " \"" +
                title + "\" ", fileName]
        subprocess.call(args)
        os.rename(fileName, title)

