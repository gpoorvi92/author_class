import os
from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 25
i=0

for root, dirs, files in os.walk("/home/purvi/author_class/chunking_text_file/40authors"):
    for dir in dirs:
	print(os.path.join(root, dir))
        dir_path=os.listdir(os.path.join(root, dir))
	mypath = os.path.join("/home/purvi/author_class/chunking_text_file/40authors_chunk_25", dir)
	if not os.path.isdir(mypath):
   	 os.makedirs(mypath)
	fold=(os.path.join(root, dir))
	for r,d,f in os.walk(fold):
		for di in d:
			infold = os.path.join(r, di)
			diro_path=os.listdir(infold)
			for eachFile in diro_path:
		 		f_path=infold+'/'+eachFile  
		 		print(f_path) 		
		 		with open(f_path) as f:
		  		#if f_path.endswith(".java"):
		   			for k,g in enumerate(grouper(n, f, fillvalue=''), 1):
		    				i+=2
		    				with open(os.path.join(mypath, '{0}.txt').format(i * n), 'w') as fout:
		     					fout.writelines(g)
		
	
