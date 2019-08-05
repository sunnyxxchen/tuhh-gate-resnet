from PIL import Image
import numpy as np

img_num = 76000
noise_sd = 10

def load_image(infilename) :
    img = Image.open( infilename )
#    img.load()
    data = np.asarray(img)
    data = data[:,:,:3]
    return data

def save_image(npdata, outfilename) :
    img = Image.fromarray(npdata, mode="RGB")
    img.save( outfilename )

def noise_image(npdata, scale):
    noise = np.random.normal(scale=scale, size=npdata.shape)
    noise += npdata
    noise = np.round(noise)
    noise = np.maximum(0, noise)
    noise = np.minimum(255, noise)
    return noise

#save_path = '/home/hippoc/bin/beauvoir/data/crop_data/

for i in range(img_num):
    im = load_image(str(i)+'.png')
    noisy = noise_image(im, noise_sd)
    noisy = noisy.astype('uint8')
    print(i)
    save_image(noisy, 'noised/'+str(i)+'.png')
