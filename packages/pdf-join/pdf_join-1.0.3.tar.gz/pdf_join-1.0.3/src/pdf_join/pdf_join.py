import sys
from tqdm import tqdm
from glob import glob

from PyPDF2 import PdfFileMerger

def flatten(l: list) -> list:
	return [i for sl in l for i in sl]

def pdf_join(files, out):
	'''
	Merges all PDFs in files in order. Globs first.
	'''
	files = [glob(file, recursive=True) for file in files]
	files = flatten(files)
	
	merger = PdfFileMerger()
	print('Merging PDFs...')
	for file in tqdm(files):
		merger.append(file)
	
	merger.write(out)

if __name__ == '__main__':
	out = [arg for i, arg in enumerate(sys.argv[1:]) if sys.argv[i-1] == '--out']
	if not out:
		out = 'merged.pdf'
	
	args = [arg for i, arg in enumerate(sys.argv[1:]) if arg not in ['pdf_join.py', '--out'] and not sys.argv[i-1] == '--out']
	pdf_join(args, out=out)
