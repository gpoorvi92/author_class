import os
import shutil, random
import numpy as np
n = 10  # chunk size
############################################### splitting into test and train files #########################################

train_per = 0.8
test_per = 0.2
main_folder = "../chunking_text_file/"     # change main folder acc to req
root = main_folder + "40authors"                     # data set
train_folder = main_folder + "40authors_test_train/train"
test_folder = main_folder + "40authors_test_train/test"
dirs = next(os.walk(root))[1]
for dir in dirs:
	dir_path = os.path.join(root, dir)
	in_dir = next(os.walk(dir_path))[1]
	in_dir_path = os.path.join(dir_path, in_dir[0])	
	mypath_train = os.path.join(train_folder, dir)
	mypath_test = os.path.join(test_folder, dir)
	if not os.path.isdir(mypath_train):
   	 os.makedirs(mypath_train)
	if not os.path.isdir(mypath_test):
   	 os.makedirs(mypath_test)
	for r_out, d_out, foldFile in os.walk(in_dir_path):
		file_count = len(foldFile)
		train_count = np.int(train_per * file_count )
		test_count = np.int(file_count - train_count)

		print(train_count)
		print(test_count)
		filenames = random.sample(os.listdir(in_dir_path), train_count)
		test_filenames = list(set(os.listdir(in_dir_path))- set(filenames))
		print(test_filenames)
		print(filenames)
		for fname in filenames:
			srcpath = os.path.join(in_dir_path, fname)
			destpath = os.path.join(mypath_train, fname)
			shutil.copyfile(srcpath, destpath)
		for fname in test_filenames:
			srcpath = os.path.join(in_dir_path, fname)
			destpath = os.path.join(mypath_test, fname)
			shutil.copyfile(srcpath, destpath)

#################################################### converting files into chunk #################################################
from itertools import izip_longest
src_train_folder = main_folder + "40authors_test_train/train"
src_test_folder = main_folder + "40authors_test_train/test"
dst_train_folder = main_folder + "40authors_test_train_chunk/train"
dst_test_folder =  main_folder + "40authors_test_train_chunk/test"
i=0	
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

########################################################### for train folder
dirs = next(os.walk(src_train_folder))[1]
print(dirs)
for dir in dirs:
	dir_path = os.path.join(src_train_folder, dir)
	print(dir_path)
	dst_path = os.path.join(dst_train_folder, dir)
	if not os.path.isdir(dst_path):
	 os.makedirs(dst_path)
	for r, d, files in os.walk(dir_path):
		for filenames in files:
			f_path = os.path.join(dir_path, filenames)
			with open(f_path) as f:
				for k,g in enumerate(grouper(n, f, fillvalue=''), 1):
					i+=2
					with open(os.path.join(dst_path, '{0}.txt').format(i * n), 'w') as fout:
						fout.writelines(g)
	


################################################### for test folder we need to main labels too
dirs = next(os.walk(src_test_folder))[1]
print(dirs)
class_count = 0
for dir in dirs:
	class_count = class_count + 1
	file_count = 0
	dir_path = os.path.join(src_test_folder, dir)
	print(dir_path)
	dst_path = os.path.join(dst_test_folder, dir)
	if not os.path.isdir(dst_path):
	 os.makedirs(dst_path)
	for r, d, files in os.walk(dir_path):
		for filenames in files:
			file_count = file_count + 1
			f_path = os.path.join(dir_path, filenames)
			with open(f_path) as f:
				for k,g in enumerate(grouper(n, f, fillvalue=''), 1):
					i+=2
					with open(os.path.join(dst_path, '{0}.txt').format(i * n), 'w') as fout:
						fout.writelines(g)
					with open('label_file', 'a') as f_label:
						f_label.writelines( dir + " " + '{0}.txt'.format(i * n)+  " " + str(file_count) + "\n")
		


