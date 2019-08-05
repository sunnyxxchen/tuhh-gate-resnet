import numpy as np
from PIL import Image, ImageDraw

f = open('labels.txt')
labels = f.readlines()
labels = [eval(x.strip()) for x in labels]
labels = np.array([(x[0]*300, x[1]*200) for x in labels])

for i in range(500):
    img = Image.open(str(i)+'.png')
    draw = ImageDraw.Draw(img)
                
    pred = labels[i]
                    
    draw.line([tuple(pred - [10, 0]), tuple(pred + [10, 0])], fill="blue", width=3)
    draw.line([tuple(pred - [0, 10]), tuple(pred + [0, 10])], fill="red", width=3)

    #    draw.point(labels_orig[i], fill="blue")
    #    draw.point(preds[i-15840], fill="black")
    img.save("orig_label/" + str(i) + "_label.png")
