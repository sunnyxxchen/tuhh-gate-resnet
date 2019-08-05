import sys
import os
beauvoir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
sys.path.append(beauvoir_path)
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
from utils.image_center_generator import ImageCenterGenerator

obj_model_directory = '../data/Gates/thin_gates/'
save_path = '../data/thin_pics/farther/'
background_path = '../data/backgrounds/'


num_images_per_class = 500
resolution = (300, 200)
background = 'crop'
max_num_lamps = 5
zoom_range = [-9, -7]
translation_range = [-2.2,2.2] 
rotation_range = [-20,20]
#translation_range = [-0.1, 0.1]
#rotation_range = [-30,30]

image_generator = ImageCenterGenerator(
                        obj_model_directory, save_path,
                        num_images_per_class=num_images_per_class,
                        resolution=resolution, 
			background=background,
                        background_images_directory=background_path,
                        max_num_lamps=max_num_lamps,
                        zoom_range=zoom_range,
			rotation_range=rotation_range,
                        translation_range=translation_range)

image_generator.render()
