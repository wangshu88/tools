#!/usr/bin/env python
#coding:utf8
import sys
import argparse

info='''
===================================================
			
            Util:     Decode Morse Code
            Author:   iFurySt
            Email:    hk326459@163.com
            Website:  www.iFurySt.com

        Usage:python morse.py '-- --- .-. ... .'

===================================================
'''

print(info)

def morse(rawData):
	morse={
	'.-' : 'A',      '-...' : 'B',       '-.-.' : 'C',
	'-..' : 'D',     '.' : 'E',          '..-.' : 'F',
	'--.' : 'G',     '....' : 'H',       '..' : 'I',
	'.---' : 'J',    '-.-' : 'K',        '.-..' : 'L',
	'--' : 'M',      '-.' : 'N',         '---' : 'O',
	'.--.' : 'P',    '--.-' : 'Q',       '.-.' : 'R',
	'...' : 'S',     '-' : 'T',          '..-' : 'U',
	'...-' : 'V',    '.--' : 'W',        '-..-' : 'X',
	'-.--' : 'Y',    '--..' : 'Z',       '-----' : '0',
	'.----' : '1',   '..---' : '2',      '...--' : '3',
	'....-' : '4',   '.....' : '5',      '-....' : '6',
	'--...' : '7',   '---..' : '8',      '----.' : '9',
	'--..--': ',',   '.-.-.-': '.',      '..--..': '?',
	'-.-.-.': ':',   '---...': ':',      '.----.': '-',
	'-..-.' : '/',   '..--.-': '()'

	}

	data=rawData.split(' ')
	result=''
	for v in data:
		result+=morse[v].lower()
	print(result)

if __name__=='__main__':
	parser=argparse.ArgumentParser(description='Decode Morse Code.')
	parser.add_argument('Morse_Code')
	args=parser.parse_args()
	if len(sys.argv)==1:
		print(parser.print_usage)
		sys.exit()
	morse(sys.argv[1])
