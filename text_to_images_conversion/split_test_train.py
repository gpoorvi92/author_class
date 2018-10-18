import os
import shutil, random
import numpy as np



from itertools import izip_longest

train_per = 0.8
test_per = 0.2

for root, dirs, files in os.walk("/home/purvi/author_classification/text_to_images_conversion/40authors_image"):
    for dir in dirs:
	print(os.path.join(root, dir))
        dir_path=os.path.join(root, dir)
	mypath_train = os.path.join("/home/purvi/author_classification/text_to_images_conversion/final_data/train", dir)
	mypath_test = os.path.join("/home/purvi/author_classification/text_to_images_conversion/final_data/test", dir)
	if not os.path.isdir(mypath_train):
   	 os.makedirs(mypath_train)
	if not os.path.isdir(mypath_test):
   	 os.makedirs(mypath_test)
	fold=(os.path.join(root, dir))
	r, d, foldFile = next(os.walk(fold))
	file_count = len(foldFile)
	train_count = np.int(train_per * file_count )
	test_count = np.int(file_count - train_count)

	print(train_count)
	print(test_count)
	print(dir_path)
	filenames = random.sample(os.listdir(dir_path), train_count)
	test_filenames = list(set(os.listdir(dir_path))- set(filenames))
	print(test_filenames)
	print(filenames)
	for fname in filenames:
    		srcpath = os.path.join(dir_path, fname)
		destpath = os.path.join(mypath_train, fname)
    		shutil.copyfile(srcpath, destpath)
	for fname in test_filenames:
    		srcpath = os.path.join(dir_path, fname)
		destpath = os.path.join(mypath_test, fname)
    		shutil.copyfile(srcpath, destpath)
	





		
	
