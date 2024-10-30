# __main__.py

import sys

from .pdf_join import pdf_join

def main():
	'''
	Run pdfmerge to merge PDFs.
	'''
	breakpoint()
	out = [arg for i, arg in enumerate(sys.argv[1:]) if sys.argv[i-1] == '--out']
	if not out:
		out = 'merged.pdf'
	
	args = [arg for i, arg in enumerate(sys.argv[1:]) if arg not in ['pdf_join.py', '--out'] and not sys.argv[i-1] == '--out']
	pdf_join(*args, out=out)

if __name__ == '__main__':
	main()