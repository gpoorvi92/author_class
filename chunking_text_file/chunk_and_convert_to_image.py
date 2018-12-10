import os
from itertools import izip_longest
import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import shutil, random
import numpy as np

train_per = 0.8
test_per = 0.2
PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"
root = "/home/purvi/author_class/chunking_text_file/40authors"
n=20

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def chunk():
	i=0
	print(next(os.walk(root))[1])
	for dir in next(os.walk(root))[1]:
		print(os.path.join(root, dir))
		dir_path=os.listdir(os.path.join(root, dir))
		mypath = os.path.join(root + "_chunk_" + str(n), dir)
		if not os.path.isdir(mypath):
		 os.makedirs(mypath)
		fold=(os.path.join(root, dir))
		for r,d,f in os.walk(fold):
			for di in d:
				infold = os.path.join(r, di)
				diro_path=os.listdir(infold)
				for eachFile in diro_path:
			 		f_path=infold+'/'+eachFile  
			 		#print(f_path) 		
			 		with open(f_path) as f:
			  		#if f_path.endswith(".java"):
			   			for k,g in enumerate(grouper(n, f, fillvalue=''), 1):
			    				i+=2
			    				with open(os.path.join(mypath, '{0}.txt').format(i * n), 'w') as fout:
			     					fout.writelines(g)
	



def main():
	chunk()	
	for roots, dirs, files in os.walk(root + '_chunk_'+str(n)):
	    for dir in dirs:
		print(os.path.join(roots, dir))
		dir_path=os.listdir(os.path.join(roots, dir))
		mypath = os.path.join(root + "_image_"+str(n), dir)
		print(mypath)
		if not os.path.isdir(mypath):
	   	 os.makedirs(mypath)
		 print("dir made")
		fold=(os.path.join(roots, dir))
		for eachFile in dir_path:
			if eachFile.endswith(".txt"):
				f_path=fold+'/'+eachFile 
				print(f_path)
				image = text_image(f_path)
				print(mypath)
				image.save('{0}.png'.format(os.path.join(mypath,eachFile)))

def text_image(text_path, font_path=None):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    text_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(text_file.readlines())

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    #max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    #c_box = PIL.ImageOps.invert(image).getbbox()
    #image = image.crop(c_box)
    #size = 128, 128
    #im = Image.open(image)
    #im_resized = image.resize(size, Image.ANTIALIAS)
    return image
 
def split_data():   
	for roots, dirs, files in os.walk(root + "_image_" + str(n)):
	    for dir in dirs:
		print(os.path.join(roots, dir))
		dir_path=os.path.join(roots, dir)
		mypath_train = os.path.join(root + "_final_data_" + str(n) + "/train" , dir)
		mypath_test = os.path.join(root + "_final_data_" + str(n) + "/test", dir)
		if not os.path.isdir(mypath_train):
	   	 os.makedirs(mypath_train)
		if not os.path.isdir(mypath_test):
	   	 os.makedirs(mypath_test)
		fold=(os.path.join(roots, dir))
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


if __name__ == '__main__':
	main()
	split_data()
