import os
import shutil

compare_folder = './image/zebra/'
target_folder = './mask/zebra/'
source_folder = 'F:\\Programming\\Git\\TF_KR\\image_attention\\dark_zebra\\'

compare_files = os.listdir(compare_folder)
target_files = os.listdir(target_folder)
for compare_file in compare_files:
	if compare_file not in target_files:
		shutil.copy(source_folder + compare_file, target_folder)
		print('Copy', compare_file)