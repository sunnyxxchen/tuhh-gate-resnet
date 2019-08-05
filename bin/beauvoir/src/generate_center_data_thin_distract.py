import sys
import os
beauvoir_path = os.path.dirname(os.path.realpath(__file__)) + '/'
sys.path.append(beauvoir_path)
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
from utils.image_center_generator_distractions import ImageCenterGenerator

obj_model_directory = '../data/Gates/thin_gates/'
save_path = '../data/thin_distract_plus/orig/'
background_path = '../data/backgrounds/'
distract = '../data/Distractions/'


num_images_per_class = 3000
resolution = (300, 200)
background = 'crop'
max_num_lamps = 5
zoom_range = [-7, 0]
translation_range = [-0.3,0.3] 
rotation_range = [-10,10]
distract_num = 25
back_distract = True
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
                        back_distract=back_distract,
                        distract_num=distract_num)

image_generator.render()
