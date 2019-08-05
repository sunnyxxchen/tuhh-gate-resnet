# tuhh-gate-resnet
## bin
contains the beauvoir code, which I used to generate the training data. Use it by running files in bin/beauvoir/src with blender --background --python generate_INSERT_FILE_HERE.py

read more about beauvoir here: https://github.com/oarriaga/beauvoir
## scripts
contains useful scripts that I used to help generate the training data
## models
contains some of the models that I have trained
## notebooks
contains the jupyter notebooks I used to train and test the models
## current workflow
what I have been doing is running the following: 
```
blender --background --python generate_center_data_close_thin_distract.py
blender --background --python generate_center_data_far_thin_distract.py
blender --background --python generate_center_data_new_thin_distract.py
blender --background --python generate_center_data_thin_distract.py
```
this will generate four sets of images: close is for when the gate is closeup, far is for when the gate is really far, new is for when the gate is somewhat far, and the last is just for a bunch of random cases.

then, I use ```scripts/combine_sets.py``` to combine these sets, ```scripts/noise.py``` to generate another set with noise, and ```scripts/combine_sets.py``` again to combine the noisy and normal sets.
