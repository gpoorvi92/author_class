import os

from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 10
i=0

dir_path=os.listdir('/home/purvi/author_classification/chunking_text_file/40authors')
fold=('/home/purvi/author_classification/chunking_text_file/40authors/chacha/chacha')

for eachFile in dir_path:
 f_path=fold+'/'+eachFile   		
 with open(f_path) as f:
  #if f_path.endswith(".java"):
   for k,g in enumerate(grouper(n, f, fillvalue=''), 1):
    i+=2
    with open('/home/purvi/author_classification/chunking_text_file/40authors_chunk/chacha/{0}.txt'.format(i * n), 'w') as fout:
     fout.writelines(g)
    

