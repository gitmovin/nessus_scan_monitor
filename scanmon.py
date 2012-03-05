#!/usr/bin/env python
# encoding: utf-8
'''
untitled.py

Created by Steven McGrath on 2012-03-04.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
'''

import sys
import getopt


help_message = '''
The help message goes here.
'''


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg


def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], 'ho:v', ['help', 'output='])
		except getopt.error, msg:
			raise Usage(msg)
	
		# option processing
		for option, value in opts:
			if option == '-v':
				verbose = True
			if option in ('-h', '--help'):
				raise Usage(help_message)
			if option in ('-o', '--output'):
				output = value
	
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split('/')[-1] + ': ' + str(err.msg)
		print >> sys.stderr, '\t for help use --help'
		return 2


if __name__ == '__main__':
	sys.exit(main())
