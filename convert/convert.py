from PIL import Image
import os

filelist = ["images/profile.jpg","images/moon.jpg"]

for infile in filelist:
    outfile = os.path.splitext(infile)[0]+".png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
                print("Cannot convert"), infile
