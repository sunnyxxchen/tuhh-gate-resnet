from shutil import copyfile
import numpy as np

#paths = ['orig/', 'far/', 'farther/', 'nearest/']
paths = ['combined/', 'combined/noised/']
save_path = '/home/hippoc/bin/beauvoir/data/thin_distract_plus/dataset/'

#nums = [48000, 6400, 8000, 8000]
nums = [70400, 70400]

comb_labels = open(save_path+"labels.txt", "w")

indices = np.arange(sum(nums))

shuffled = np.arange(sum(nums))
np.random.shuffle(shuffled)

lines = list(np.zeros(sum(nums)))

ind = 0
for i, path in enumerate(paths):
    labels = open(path+"labels.txt", 'r')
    labels = labels.readlines()
    for j in range(nums[i]):
        new_ind = shuffled[ind]
        copyfile(path+str(j)+'.png', save_path+str(new_ind)+'.png')
        lines[new_ind] = labels[j]
        print(ind)
        ind += 1
       
[comb_labels.write(i) for i in lines]
