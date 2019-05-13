#!/usr/bin/env python3
#
# by dash in 2019
############################


import os
import sys
import argparse
import threading

from lib.FUDGEanalyse import *
from lib.FUDGEheader import *

#maybe put that later somewhere else
extractit=0
fileReport=0

def fudge_banner():
	ff=ANALYSE()
	print ("[+] FirmareFudger %s by dash" % ff.__version__)
	print ("[+] tool for firmware analyses, May 2019")
	print ("[+] ")
	print ("[+] contact: d4shmail@gmail.com")
	print
	ff=[]

def ff_fudge_routine(ff):
	''' the classic ffudger routine 
		patched and fixed up a bit :)
	'''
	#print the banner :D
	#fudge_banner()


	# print some basic information
	ff.printargs()

	true=0
	# check if only one plugin shall be tested
	if ff.lonelyplugin!=None:
		lonely=ff.lonelyplugin
		for category in FUDGEheader.TYPES.keys():
			for plugin in FUDGEheader.TYPES[category].keys():
				if ff.lonelyplugin == FUDGEheader.TYPES[category][plugin][FUDGEheader.NAME]:
					print ('[+] Analyzing for %s' % ff.lonelyplugin)
					# checkheader etc.pp.
					ff.fftype=lonely

					# fill the targetqueue	
					ff.ff_fill_targetqueue(category,plugin)

					# run the check routine
					ff.checkheader()

	# check if only a group shall be tested
	elif ff.ff_cat!=None:

		if ff.ff_cat in FUDGEheader.TYPES_DEF:
			#print (ff.ff_cat)
			category=FUDGEheader.TYPES_DEF[ff.ff_cat]

			#only check for the asked TYPE
			print ("[+] Testing only for %s plugins" % (ff.ff_cat))
			for plugin in range(len(TYPES[category])):
				# fill the targetqueue	
				ff.ff_fill_targetqueue(category,plugin)

				# check the file
				ff.checkheader()

		else:
			print ("[-] Unkown plugin class %s !" % ff.plugin)
			sys.exit(1)

			
	# if not one_plugin is choosen and also not the ff_cat
	# we do check for all FF plugins 
	elif ff.ff_cat == None and ff.lonelyplugin==None:	
		print ('[+] Checking for all FF plugins')

		#check for all TYPES
		for category in range(len(TYPES)):
			#print (len(TYPES))

			#print (TYPES[category])
			for plugin in range(len(TYPES[category])):
				#print (len(TYPES[testtype]))

				# set the fftype
				ff.fftype=TYPES[category][plugin][3]

				# fill the targetqueue	
				ff.ff_fill_targetqueue(category,plugin)

				# call the check_routine
				#ff_check_routine(ff)
				ff.checkheader()

	# ok, something went wrong
	else:

	# was not able to find the named plugin
		print ('[-] Sorry, something went wrong.\n[?] Execute tool with -Fl to see a complete fudger plugin list.')
		return 1;
	
	# If a report needs to be created, create it now
	#generateFilereport(ff)

	#print (ff.result_queue.qsize())

	# hm, should work :>
	while True:
		if len(ff.thread_list)>0:
		#	print ('[.] Waiting for threads to finish %d' % (len(ff.thread_list)))
			time.sleep (0.1);
			for entry in ff.thread_list:
				if (entry.isAlive())==False:
					entry.join()
					ff.thread_list.remove(entry)
		else:
			break
				
	# If extract data has been choosen, extract it now
	ff.extractdata()

	# do strings analysis
	if ff.str_analysis:
		ff.strings_search()

	return 0;


def run(args):
	''' main run function, let the fun begin'''

	# instanciate FUDGEanalysis Class
	ff=ANALYSE()

	# Preparations before we can analyse a file

	# set threads if given
	if args.threads:
		ff.thread_cnt=args.threads

	# show FirmwareFudgers Plugin Database, and return
	if args.fudgelist:
		ff.showplugins()
		return 0;

	# show FirmwareFudgers Plugin Database, and return
	#print (args.fudgelist_cat)
	if args.fudgelist_cat:
		ff.showplugins(cat=args.fudgelist_cat)
		return 0;

	# set the file to analyse
	if args.infile:
		ff.infile=args.infile


	# set the prefix for every extracted file
	# default: FF-Extract 
	if args.outprefix:
		ff.outprefix=args.outprefix

	# set the output directory
	if args.outdir:
		ff.outdir=args.outdir
		# check if directory exists, if not create it
		# if an error comes along, we abort the complete operation
		if not ff.create_dir():
			print ('[-] Abort.')

	# create a report
	if args.create_report:
		ff.create_report=args.create_report

	# use only one specific plugin
	ff.lonelyplugin=args.lonelyplugin

	# use only specific plugin group
	ff.ff_cat=args.ff_cat

	# set extract to true
	if args.extract:
		ff.extract=True
		ff.create_dir()


	# set verbose mode
	if args.verbose:
		ff.verbose=True 

	# set debug mode
	if args.debug:
		ff.debug=True
	
	# show version
	#print (args.version)
	if args.version==True:
		fudge_banner()
		return 0;

	# add flag if strings analysis is wanted
	if args.strings == True:
		ff.str_analysis=True
		ff.str_minlen=args.str_minlen
		ff.str_filter=args.str_filter
 
	# try to open our target file
	if ff.openfile()==-1:
		sys.exit(1)

 	# use ff method
	if args.fudge:
		ff_fudge_routine(ff)


def main():
	''' yay, we got a main :)'''

	ff=ANALYSE()
	__tool__ = ff.__tool__
	__version__ = ff.__version__
	__author__ = ff.__author__
	__date__ = ff.__date__

	parser_desc = 'FirmwareFudger, written to do better firmware analysis'
	prog_desc = __tool__ + ' v' + __version__ + ' by ' + __author__ + ' (' + __date__ + ')'
	parser = argparse.ArgumentParser(prog = prog_desc, description=parser_desc)
	parser.add_argument('-f','--input-file',action="store",dest='infile',required=False,help='define the file to analyze')
	parser.add_argument('-o','--outdir',action="store",dest='outdir',required=False,help='define the directory to save extracted files and logs to')
	parser.add_argument('-O','--output-prefix',action="store",dest='outprefix',required=False,help='define the prefix for the extracted name (default: FF-Extract)')
	parser.add_argument('-x','--extract',action="store_true",dest='extract',required=False,help='flag if you want to extract found files', default=False)
	parser.add_argument('-F','--fudge',action="store_true",dest='fudge',required=False,help='use fudge mode (FirmwareFudgers own database)',default=True)
	parser.add_argument('-S','--strings',action="store_true",dest='strings',required=False,help='run strings on file and conduct analysis',default=False)
	parser.add_argument('-Sl','--strings-len',action="store",dest='str_minlen',required=False,help='the minimum length for string check',default=4, type=int)
	parser.add_argument('-Sf','--strings-filter',action="store",dest='str_filter',required=False,help='the strings check filter, use regular expressions',default="([a-zA-Z0-9 \.\-]{7,})")
	parser.add_argument('-M','--magic',action="store_true",dest='magic',required=False,help='use magic mode (libmagic database)',default=True)
	parser.add_argument('-Fp','--fudge-plugin',action="store",dest='lonelyplugin',required=False,help='run only one specified plugin test',default=None)
	parser.add_argument('-Fc','--fudge-category',action="store",dest='ff_cat',required=False,help='run only a section of possible plugins (e.g. EXEC)',default=None)
	parser.add_argument('-Fl','--fudge-list',action="store_true",dest='fudgelist',required=False,help='show plugins of FirmwareFudger',default=False)
	parser.add_argument('-Flc','--fudge-list-cat',action="store",dest='fudgelist_cat',required=False,help='show plugins of defined group',default=False)
	parser.add_argument('--threads',action="store",dest='threads',required=False,help='define the value of maximum threads used, default is 20',default=None,type=int)
	parser.add_argument('-v','--verbose',action="store_true",dest='verbose',required=False,help='run in verbose mode',default=False)
	parser.add_argument('--debug',action="store_true",dest='debug',required=False,help='run in debug mode',default=False)
	parser.add_argument('-r','--report',action="store_true",dest='create_report',required=False,help='create a report for the session',default=False)
	parser.add_argument('-V','--version',action="store_true",dest='version',required=False,help='show version and tool information',default=False)

	args = parser.parse_args()

	# if no argument is given help is printed
	if len(sys.argv)<2:
		parser.print_help()
		sys.exit(1)

	run(args)

if __name__ == "__main__":
	main()
