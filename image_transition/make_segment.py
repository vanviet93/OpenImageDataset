import numpy as np
import os
import cv2
layers = {
	'Sky': np.float32([127,0,0]), 
	'Cloud': np.float32([255,255,255]), 
	'Water': np.float32([255,0,0]), 
	'Mountain': np.float32([0,76,76]), 
	'Ground': np.float32([76,76,76]), 
	'Grass': np.float32([0,255,0]), 
	'Tree': np.float32([0,127,0])}
UNIDENTIFIED_LAYER_COLOR = np.float32([0,0,0])
full_folder = './full/'
part_folder = './part/'
target_folder = './segment/'
image_files = os.listdir(full_folder)
image_files = [image_file for image_file in image_files if image_file.endswith('xcf')]
image_names = [image_file[:-4] for image_file in image_files]
for image_name in image_names:
	print('--------------')
	print(image_name)
	image = None
	for i, layer in enumerate(layers):
		image_path = part_folder + image_name + '_' + layer + '.png'
		print(image_path)
		if not os.path.exists(image_path):
			continue
		layer_image = cv2.imread(image_path)
		gray = np.mean(layer_image, axis=2)
		if image is None:
			h, w, _ = layer_image.shape
			image = np.zeros([h, w, 3], dtype=np.uint8)
		for m in range(h):
			for n in range(w):
				if gray[m,n]>10:
					image[m,n] = layers[layer]
	print('Image name', image_name)
	print('Image', image.shape)
	cv2.imwrite(target_folder + image_name + '.png', image)