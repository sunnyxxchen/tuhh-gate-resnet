import os
from PIL import Image

for filename in os.listdir():
    split_filename = filename.split(".")
    if split_filename[1] == "jpg":
        print(filename)
        im = Image.open(filename)
        (width, height) = (round(im.width * 0.8), round(im.height * 0.8))
        im_resized_big = im.resize((width, height))

        (width, height) = (round(im.width * 0.5), round(im.height * 0.5))
        im_resized = im.resize((width, height))
        im_resized.save("../backgrounds/" + split_filename[0] + "_resized" + ".png")
        im.save("../backgrounds/" + split_filename[0] + ".png")
