import sys
import os

path = '/home/hippoc/bin/beauvoir/data/crop_data/300x200/test/preds_cpu/'

#if len(sys.argv) == 1:
#    raise BaseException("no number of images given")

#elif len(sys.argv) > 2:
#    raise BaseException("too many arguments")

ins = 0
outs = 0
edges = 0

for filename in os.listdir(path):
    split_filename = filename.split(".")

    if not split_filename[1] == "png":
        print(filename)
        continue

    os.system("shotwell " + path + filename + "&")
    valid_input = False
    while not valid_input:
        s = input("image " + filename + ":")
        if s == "i":
            ins += 1
            valid_input = True
        elif s == "o":
            outs += 1
            valid_input = True
        elif s == "e":
            edges += 1
            valid_input = True
        elif s == "na":
            valid_input = True
        print('\n')

    os.system("killall shotwell")
#        else:
#            raise BaseException('error')

print("ins: ", ins, "outs: ", outs, "edges: ", edges)
