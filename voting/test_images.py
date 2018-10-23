from __future__ import print_function
from __future__ import division
import keras
import os
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, load_img
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

######################################### create labels for test images and write in predict_label_file ###################

def predict_labels_for_test_files_from_saved_model():
	validation_dir = '/home/purvi/author_class/voting/40authors_test_train_image/test'
	image_size = 256



	from keras import models
	from keras import layers
	from keras import optimizers
	from keras.preprocessing import image


	saved_model_path = 'all_freezed.h5'
	exists = os.path.isfile(saved_model_path)
	model = load_model(saved_model_path)
	print ("Loading existing model")

	dirs = next(os.walk(validation_dir))[1]
	print(dirs)
	i=0
	n=10
	for dir in dirs:
		file_count = 0
		dir_path = os.path.join(validation_dir, dir)
		print(dir_path)
		for r, d, files in os.walk(dir_path):
			for filenames in files:
				f_path = os.path.join(dir_path, filenames)
				test_image = image.load_img(f_path, target_size = (image_size, image_size))
				test_image = image.img_to_array(test_image)
				test_image = np.expand_dims(test_image, axis=0)
				result = model.predict(test_image)
				predict = dirs[np.argmax(result[0])]
				with open('predict_label_file', 'a') as f_label:
					f_label.writelines(  filenames+  " " + dir + " " + predict + "\n" )


####################################### create common list from actual and predicted labels #######################################

from itertools import groupby
from operator import itemgetter

def inner_join(a, b):
	L = a + b
	len_A = len(a)
	len_B = len(b)
	final_list = []
	L.sort(key=itemgetter(0)) # sort by the first column
	for lis in range(0, len_A):
		row_A = L[lis]
		row_B = L[len_B]
		row_A[-1] = row_A[-1].strip()
		row_B[-1] = row_B[-1].strip()
		len_B = len_B + 1
		with open('final_label_file', 'a') as f_label:
			f_label.writelines( row_A[1]+ " " + row_A[2] + " " + row_A[3] + " " + row_B[3] +  "\n" )
  


def compare_actual_and_predicted_label_files():
	my_list_actual = [line.split(' ') for line in open("label_file")]
	my_list_predicted = [line.split(' ') for line in open("predict_label_file")]
	result = list(inner_join(my_list_actual, my_list_predicted))
	#print(my_list_predicted)
	print(result)

############################################ find actual labels after voting ######################################################### 

def final_accuracy():
	final_list = [line.split(' ') for line in open("final_label_file")]
	len_list = len(final_list)
	total_file_count = 1
	correct_file_count = 0
	total_chunks_in_file = 1
	correct_chunks_in_file = 0
	end = 0
	for li in range(0, len_list-1):
		print(li)
		row_A = final_list[li]
		row_A[-1] = row_A[-1].strip()
		row_B = final_list[li + 1]
		row_B[-1] = row_B[-1].strip()
		if(row_A[1] == row_B[1] and row_A[2] == row_B[2]):  # both belong to same file
			total_chunks_in_file = total_chunks_in_file + 1
			if(row_A[1] == row_A[3]):                   # first chunk is classified correctly
				correct_chunks_in_file = correct_chunks_in_file + 1
			if(li == (len_list-2)):
				print(len_list)
				print(correct_file_count)
				print(correct_chunks_in_file)
				print("hello")
				if(row_B[1] == row_B[3]):
					print("hi")						
					correct_chunks_in_file = correct_chunks_in_file + 1
					print(correct_chunks_in_file)
					print(total_chunks_in_file)
					print(np.float(correct_chunks_in_file/total_chunks_in_file))
					if(np.float(correct_chunks_in_file/total_chunks_in_file) > 0.51):
						print("correct")
						correct_file_count = correct_file_count + 1
					end = 1
		else:  						    # both belong to different chunks
			total_file_count = total_file_count + 1     # increment number of files
			if(row_A[1] == row_A[3]): # prev pred c										
				correct_chunks_in_file = correct_chunks_in_file + 1
			print(np.float(correct_chunks_in_file/total_chunks_in_file))
			if(np.float(correct_chunks_in_file/total_chunks_in_file) > 0.51):
				print("correct")
				correct_file_count = correct_file_count + 1			
			total_chunks_in_file = 1
			correct_chunks_in_file = 0
	if(end==0):
		row_A = final_list[len_list-1]
		if(row_A[1] == row_A[3]):
			correct_file_count = correct_file_count + 1
	print("----------------------------------------------------------")
	print(total_file_count)	
	print(correct_file_count)	
	acc = np.float(correct_file_count * 100 / total_file_count )
	print(acc)
				




#predict_labels_for_test_files_from_saved_model()
#compare_actual_and_predicted_label_files()
final_accuracy()
