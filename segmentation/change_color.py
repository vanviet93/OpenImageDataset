import os
import cv2
import numpy as np
tag = 'dog'
source_folder = './image/' + tag + '/'
target_folder = './mask/' + tag + '/'
for file in os.listdir(source_folder):
	img = np.float32(cv2.imread(source_folder + file))
	img = img / 2
	cv2.imwrite(target_folder + file, img)
	print(target_folder + file)