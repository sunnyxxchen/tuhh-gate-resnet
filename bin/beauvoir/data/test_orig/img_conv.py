import os

import os
from PIL import Image

for filename in os.listdir():
    split_filename = filename.split(".")
    if split_filename[1] == "jpg":
        print(filename)
        im = Image.open(filename)
        (width, height) = (round(im.width * 0.6), round(im.height * 0.6))
        im_resized = im.resize((width, height))
        im_resized.save("../test_backgrounds/" + split_filename[0] + "_resized" + ".png")
        im.save("../test_backgrounds/" + split_filename[0] + ".png")
