import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
import os
from PIL import Image

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"

def main():
	
	for root, dirs, files in os.walk('/home/purvi/author_class/chunking_text_file/40authors_chunk_25'):
	    for dir in dirs:
		print(os.path.join(root, dir))
		dir_path=os.listdir(os.path.join(root, dir))
		mypath = os.path.join("/home/purvi/author_class/text_to_images_conversion/40authors_image_25", dir)
		print(mypath)
		if not os.path.isdir(mypath):
	   	 os.makedirs(mypath)
		 print("dir made")
		fold=(os.path.join(root, dir))
		for eachFile in dir_path:
			if eachFile.endswith(".txt"):
				f_path=fold+'/'+eachFile 
				print(f_path)
				image = text_image(f_path)
				print(mypath)
				image.save('{0}.png'.format(os.path.join(mypath,eachFile)))
			 		

	#fold=('/home/purvi/text_to_image-0.0.5/text_to_image')

       	#for eachFile in dir_path:
	#	if eachFile.endswith(".txt"): #specified extension as it was picking up unwanted stuff
	#		f_path=fold+'/'+eachFile	   		
	#		image = text_image(f_path)
	 #   		#image.show()
	  #  		image.save('{0}.png'.format(f_path))

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
    
    	


if __name__ == '__main__':
    main()


