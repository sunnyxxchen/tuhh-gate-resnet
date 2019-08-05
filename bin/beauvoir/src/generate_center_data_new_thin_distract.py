import sys
import os
beauvoir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
sys.path.append(beauvoir_path)
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
from utils.image_center_generator_distractions import ImageCenterGenerator

obj_model_directory = '../data/Gates/thin_gates/'
save_path = '../data/thin_distract_plus/far/'
background_path = '../data/backgrounds/'
distract = '../data/Distractions/'


num_images_per_class = 400
resolution = (300, 200)
background = 'crop'
max_num_lamps = 5
zoom_range = [-7, -6]
translation_range = [-1.8,1.8] 
rotation_range = [-20,20]
distract_num = 40
distract_range = [-4, 3.5]
back_distract=True
#translation_range = [-0.1, 0.1]
#rotation_range = [-30,30]

image_generator = ImageCenterGenerator(
                        obj_model_directory, save_path, distract,
                        num_images_per_class=num_images_per_class,
                        resolution=resolution, 
			background=background,
                        background_images_directory=background_path,
                        max_num_lamps=max_num_lamps,
                        zoom_range=zoom_range,
			rotation_range=rotation_range,
                        translation_range=translation_range,
                        distract_range=distract_range,
                        back_distract=True,
                        distract_num=distract_num)

image_generator.render()
