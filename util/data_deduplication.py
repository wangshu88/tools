#!/usr/bin/env python
#coding:utf8
#Author:iFurySt
#Date:Aug 15,2016

import argparse
import sys

def run(infile,outfile):
	outfile = 'output.txt' if not outfile else outfile
	with open(infile,"r+") as fin:
		# print(fin.readlines())
		sourceData=fin.readlines()
		sourceData[-1]+='\n'
		processedData=set(sourceData)
		with open(outfile,"w+") as fout:
			fout.writelines(processedData)


if __name__=='__main__':
	parser=argparse.ArgumentParser(description='Data de-dupication by row.')
	parser.add_argument('-i','--input',help='The input file name.')
	parser.add_argument('-o','--output',help='The output file name. Default is output.txt int current directory')
	args=parser.parse_args()
	if len(sys.argv)==1:
		parser.print_usage()
		sys.exit()
	run(args.input,args.output)