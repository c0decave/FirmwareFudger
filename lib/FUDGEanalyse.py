
import re
import os
import sys
import queue
import time
import struct
import binascii
import threading

import lib.FUDGEheader as FUDGEheader
from lib.FUDGEheader import TYPES

nor=0x1
ver=0x2
dbg=0x3

def dbgprint():
    print ("nothing")

class ANALYSE(object):
	
	def __init__(self):
		
		""" 	
			infile		- the file to analyse	
			stat 		- os.stat results of self.infile 
			fftype 		- the current type of pattern test
			plugin		- choosen pluginclass to test for
			lonelyplugin- choosen lonely plugin for test
			fd 			- the filedescriptor of open and close
			search 		- the search string/bytes
			string 		- for convert2hex
			data		- the binary data field, where the bytes are filled in
			offset		- the offset delivered back for writing to self.cut
			extract_cnt	- number of the found files in file
			extract		- shall we extract anything?
			cut			- dict for offsets for the extractfile method
			outdir		- output directory for putting files
			outname		- name of the output files part
			reportfile 	- name of the status report
			files 		- list with paths of extracted files
			"""
	
		# not in use yet
		# self.threads = []			# list of overall threads
		# self.thread_cnt = 20		# amount of threads
 
 		# erm, check what those are used for :>
		self.string=""
		self.data=[]

		# ff magic search variables
		# FIXME must get cleaned up 
		self.target_queue=queue.Queue()		# all plugins to test
		self.result_queue=queue.Queue()		# all results from the test
		self.offset=0						# offset for self.cut, does not need to be global
		self.cut={}							# this will be replaced with result_queue
		self.set_offset=0					# ??
		self.set_string=0					# ??
		self.length=0						# does not need to be global, can also migrate to local

		# category and plugin variables
		# what a MESS, this *must* get cleaned up
		# FIXME
		self.fftype=None			# type of the pattern test, see header files
		self.ff_cat=None			# category to test for
		self.plugin=None			# pluginclass to test for
		self.lonelyplugin=None		# one plugin test only, named lonely plugin
		self.search=None

		# threading variables
		self.thread_cnt=20			# default value of concurrent threads is 20
		self.thread_alive=0			# variable for actually running threads
		self.thread_list=[]			# list for all active threads, not active gets removed

		# file variables
		self.fd=None				# filedescriptor of target file
		self.instat=None			# results of os.stat against infile
		self.infile=None			# the file to analyze

		# output variables
		self.outdir=None			# output directory
		self.outprefix="FF-Extract"	# prefix of every file written to output directory

		# reporting variables	
		self.report=False			# generate report if variable is True
		self.reportname=None		# name of the status report file
		self.reportfiles=[]			# list of files extracted files, for reporting

		# logging options
		self.debug=False
		self.verbose=False

		# extraction variables 
		self.extract=False			# extract found files if variable is True
		self.extract_cnt=0			# number of files found 


		# variables for strings search mechanism
		self.str_analysis=False
		self.str_minlen=4
		self.str_filter="([a-zA-Z0-9 \.\-]{"+str(self.str_minlen)+",})"
		self.str_resdict={}
		self.str_anadict={}

		# misc tool variables
		self.__author__="dash"
		self.__version__="0.5.2"
		self.__tool__="FirmwareFudger"
		self.__date__="May of 2019"


	def privileges(self):
		if self.stat.st_uid != os.getuid():
			print ("[!] Attention file owner is %d" % self.stat.st_uid)
			return False;
		else:
			return True;

	def ffprint(self,data,level): 
		''' printing wrapper for:
			* normal
			* verbose
			* debug 
			output
		'''

		if self.verbose==True and level==ver:
			print (data)
		elif self.debug==True and level==dbg:
			print (data)
		elif level==nor:
			print (data)

		return 0;

	def printargs(self):
		''' output information about the file
		'''

		size=self.instat.st_size
		Kilo=1024.0
		Mega=1048576.0

		print ("[+] Fudger Version %s - Fileinformation" % self.__version__)
		print ("[+] Filename %s" % self.infile)

		if size<=Mega:
			sizeK=size/Kilo
			print ("[+] Size %.2fK - %dB" % (sizeK,size))

		elif size>=Mega:
			sizeM=size/Mega
			sizeK=size/Kilo
			print ("[+] Size %.2fM - %.2fK - %dB" % (sizeM,sizeK,size))
		else:
			print ("[+] Size %d" % size)

		print ("[+] User %d" % self.instat.st_uid)
		print ("[+] Group %d" % self.instat.st_gid)
		#print "[+] Search for %s" % self.search

	def openfile_fd(self):
		''' simple open file operation and return fd
		'''
		
		try:
			self.instat=os.stat(self.infile)
			#print ("[+] Open %s" % (self.infile))
			fd=open(self.infile,"rb")
		except PermissionError as e:
			print ('[-]',e)
			return -1
		except IsADirectoryError as e:
			print ('[-]',e)
			return -1
		except FileNotFoundError as e:
			print ('[-]',e)
			return -1

		return fd;
	
	def openfile(self):
		''' simple open file operation
		'''
		
		try:
			self.instat=os.stat(self.infile)
			print ("[+] Open %s" % (self.infile))
			self.fd=open(self.infile,"rb")
		except PermissionError as e:
			print ('[-]',e)
			return -1
		except IsADirectoryError as e:
			print ('[-]',e)
			return -1
		except FileNotFoundError as e:
			print ('[-]',e)
			return -1
			
	def closefile(self):
		''' simple closefile operaiton'''

		print ("[+] Close %s" % self.infile)
		self.fd.close()
	
	def create_dir(self):
		''' method for checking outdir and properties
			and order creation
		'''
		if self.outdir != None:
			try:
				result=os.stat(self.outdir)
				return 0;

			except FileNotFoundError as e:
				self.__create_dir()
		elif self.outdir==None and self.extract==True:
			# self.outdir is not specified, but it has been asked to extract data
			# let us generate a directory for that usecase
			dirname = self.infile.replace('/','_')
			dirname = dirname.replace('..','_')
			dirname = dirname.replace('.','_')
			dirname = dirname.replace('!','_')
			dirname = dirname.replace('-','_')
			dirname = dirname.lower()
			self.outdir=dirname
			try:
				result=os.stat(self.outdir)
				return 0;

			except FileNotFoundError as e:
				self.__create_dir()
				return 0;


			

			

	def __create_dir(self):
		''' this function tests if the output directory does exist, if not a new
			one is created. if the name exists but it is not a directory 
			an error is thrown and the process is aborted.
		'''

		try:
			print ("[+] Creating directory %s" % (self.outdir))
			os.mkdir(self.outdir)
			return(0)
		except OSError as e:
			print ("[-] Error %d %s" % (e.args[0], e.args[1]))
			return(1)
	
	def convert2array(self):
		
		for byte in range(len(self.string)):
			print ("\'%c\'," % self.string[byte],)
	
	def ff_fill_targetqueue(self,category,plugin):
		''' here starts the calls for the magic behind the scenes
			category and plugin type are delivered and the target queue is build up

			self.target_queue - consists of all information necessary for finding magic and
			later extraction
		'''
		#   print (TYPES[testtype][plugin])
		header1=TYPES[category][plugin][1]
		header2=TYPES[category][plugin][2]
		name=TYPES[category][plugin][3]
		desc=TYPES[category][plugin][4]
		suffix=TYPES[category][plugin][5]

		# now fill up the target queue 
		self.target_queue.put({	'category':category,\
								'plugin':plugin,\
								'Header1':header1,\
								'Header2':header2,\
								'name':name,\
								'desc':desc,\
								'suffix':suffix})

		#print (self.target_queue.qsize())
		return 0;

	
	def __checkheader(self,target):
		''' new version of checkheader, that time with impressive speed 
			as a simpler search algorithm is used and an awesome class: re
			and not working :(
		'''

		fd=self.openfile_fd()
		
		#print ('[d] __checkheader')

		header1=target['Header1']
		category=target['category']
		plugin=target['plugin']
		suffix=target['suffix']
		name=target['name']
		hh=''
		cut={}

		# due a not sooo good design of ff database this has to be done
		# obviously ff database needs a redesign :)
		for i in header1:
			hh = hh+i

		# lets create our re pattern
		hh = re.escape(hh)
		hh=bytes(hh,'latin-1')
		re_comp=re.compile(hh)

		#print ('[v] Checking %s' % target['name'])
		#print ('[d] Header1:',header1)
		#print ('[d] HH:',hh)

		for match in re.finditer(re_comp, fd.read()):
		#print('match', match.span())
		#print('match.group',match.group())

			offstart, offend = match.span()
			print ("[+] FOUND %s at Offset %d to %d" % (target['name'],offstart,offend))
			#print(match.span(), match.group())
			dataend=self.instat.st_size
			cut={'offstart':offstart,'offend':offend,'dataend':dataend,'category':category,'plugin':plugin,'suffix':suffix}
			#print ('checkheader:',cut)
			self.result_queue.put(cut)
#			self.str_resdict[match.span()]=match.group()

			cut={}
			self.extract_cnt+=1

		fd.close()
	
	def checkheader(self):
		''' threaded checkheader wrapper
		'''

		while self.target_queue.qsize()>0:
			# set current thread count
			self.thread_alive=len(self.thread_list)
			# check if we have crossed the limit of maximum threads
			if self.thread_alive<self.thread_cnt:

				# get a value from the target queue
				target=self.target_queue.get()
				# set variables for the thread, make it daemon and start it
				thrd = threading.Thread(target=self.__checkheader,args=(target,))
				thrd.daemon=True
				thrd.start()

				# add the thread to our list
				self.thread_list.append(thrd)
				#print ('thrd cnt: %d' % len(self.thread_list))
			
			# this part watches that dead threads can join and it is removed from the list
			for entry in self.thread_list:
				if entry.isAlive()==False:
					entry.join()
					self.thread_list.remove(entry)

	def seekinto(self):
		allbytes=""
		self.fd=open(self.infile,"rb")
		self.fd.seek(0,0)
		self.fd.seek(self.set_offset,0)
		for byte in self.fd.read(self.length):
			byte=binascii.hexlify(byte)
			allbytes=allbytes + "\\x"+byte
		print ("%s" % allbytes,)


	def manglefile(self):
		mangle_file=open(self.infile,"r")
		for part in range(self.extract):
			mangle_file.seek(0,0)
			mangle_file.seek(self.cut[part],0)
			readbytes=mangle_file.read(8)
			print ("read %s " % readbytes)
			mangle_file.close()	
			mangle_file=open(self.infile,"r+")
			mangle_file.seek(0,0)
			mangle_file.seek(self.cut[part],0)
			mangle_file.write(self.set_string)
		mangle_file.close()	

	def extractcount(self):
		''' let's print some information about the files to extract
		'''
		print ("[+] Found %d possible types" % (self.extract_cnt))
		return 0;

	def extractdata(self):
		''' simple wrapper function, which gets called by program
		'''
    	# ram some info
		self.extractcount()

		# lets go to file extraction
		self.extractfile()
		return 0;

	def extractfile(self):
		""" its working just need some cleanups, and small fixes """	

		if self.extract_cnt == 0:
			self.ffprint('[-] Sorry, nothing to extract. Counter is zer0.',nor)
			return -1;

		if self.extract==False:
			return -1

		exo_file=open(self.infile,"rb")

		# as long as we have results in the queue
		while self.result_queue.qsize()>0:

			# place result in target variable
			target = self.result_queue.get()

			#cut[self.extract_cnt]=(offstart,offend,dataend,category,plugin,suffix)

#			print (target)
#			print (len(target))

			offstart=target['offstart']
			suffix=target['suffix']
			if suffix==None:
				suffix=''

			# go to start of file
			exo_file.seek(0,0)
			exo_file.seek(offstart,0)

			#print (self.cut)
			#print (self.cut[part])

			FILENAME=self.outdir+"/"+self.outprefix+"-"+str(self.extract)+"-"+str(offstart)+"." + suffix
			print ("[+] FILENAME: %s" % FILENAME)
			try:
				exw_file=open(FILENAME,"wb")
		
			except PermissionError as e:
				print ('[-] ',e)
				return -1;

			# data to write to the extracted file
			# please note that currently the end of the 
			# original file is the end - for reasons ;)
			TOWRITE=(self.instat.st_size)-offstart
			
			# depending on the file size this might get problematic
			buf = exo_file.read()
			exw_file.write(buf)
			
			# close the file
			exw_file.close()

			#lets add it to files if reportfile shall be written
			self.reportfiles.append(FILENAME)

	def generateReport(self):
	    print ("[+] Found %d extracted files" % len(self.files))
	    print 
	    print ("file Report")
	    print ("="*11)
	    for extracted in self.files:
		    #print "[+] %s " % extracted
		    os.spawnl(os.P_WAIT,"/usr/bin/file","file",extracted)
	
	def __print_categories(self):
		''' sub-method for printing all categories
		'''
		print ('[+] Categories')
		for cat in FUDGEheader.TYPES_DEF:
			print ('\t%s' % cat)

		return 0;

	def showplugins(self,cat=None):
		"""	all plugins currently supported by FF own database
				
		"""
		i=0
		if cat!=None:
			if cat in FUDGEheader.TYPES_DEF:
				print ("[+] Plugins:")
#				print ('[v] FOUND %s' % cat)
				catid = FUDGEheader.TYPES_DEF[cat]

				print ("[+] %s:" % cat)
				for plugin in range(len(FUDGEheader.TYPES[catid])):
					print ("\t\t- %s - %s" % (FUDGEheader.TYPES[catid][plugin][FUDGEheader.NAME],FUDGEheader.TYPES[catid][plugin][FUDGEheader.DESC]))
					i+=1

			else:
				print ('[-] Category "%s" does not exist' % cat);
				self.__print_categories()
				return -1;

		# show all plugins supported
		else:
			for fftype in range(len(FUDGEheader.TYPES)):
				if fftype==0:
					stringtype="FS"
				elif fftype==1:
					stringtype="EXEC"
				elif fftype==2:
					stringtype="PACKERS"
				elif fftype==3:
					stringtype="DOCS"
				elif fftype==4:
					stringtype="BOOT"
				elif fftype==5:
					stringtype="ASM"
				elif fftype==6:
					stringtype="PICTURES"
				elif fftype==7:
					stringtype="DEVICES"
				elif fftype==8:
					stringtype="CRYPTO"
		#		elif fftype==9:
		#			stringtype="CRYPTO"
				print ("%s:" % stringtype)
				for plugin in range(len(FUDGEheader.TYPES[fftype])):
					print ("\t\t- %s - %s" % (FUDGEheader.TYPES[fftype][plugin][FUDGEheader.NAME],FUDGEheader.TYPES[fftype][plugin][FUDGEheader.DESC]))
					i+=1

		print ("\n[+] Found %d plugins." % i)
		print ("[+] Done")

#####################################
#									#	
# 		strings analysis section	#
#									#	
#####################################

	def strings_analysis(self):
		''' method for analysing and giving hints to the analyst

			self.str_resdict, the result dictionary of self.string_search method
			self.str_anadict, the reuslt dictionary for self.string_analysis method
		'''

		ana = open('supply/strings.txt','r')
		# read strings supply file
		for line in ana.readlines():
			# is it a comment, no? then proceed
			if not line.startswith('#'):
				a = line.split(';')
				needle=a[0]
				desc=a[1]
				tools=a[2]
				for k in self.str_resdict.keys():
					if self.str_resdict[k].find(needle)!=-1:
						self.str_anadict[needle]=(needle,desc,tools)
						print ('[+] %s - %s - %s' % (needle,desc,tools))

		print ('[+] Found %d interesting string(s) during analysis.' % len(self.str_anadict))

		ana.close()
		return 0;

	def strings_output(self):
		''' method for writing results of strings search
			self.str_resdict, the result dictionary of self.string_search method
		'''

		return 0;

	def strings_search(self):
		''' this method does the work of the unix userland tool "strings"
			it searches a binary for possible strings, for later manual
			analysis. in this particular case an automatic analysis is added
			as well to hint the analyst on something interesting found

			self.str_minlen, the default is 4
			self.str_filter, the regular expression filter
			self.str_resdict, the result dictionary with string, start/end position
		'''
		# variables for strings search mechanism

		self.openfile()
	#	print (re.findall(re_filter, str(self.fd.read())))

		for match in re.finditer(self.str_filter, str(self.fd.read())):
			#print('match', match.span())
			#print('match.group',match.group())
#			print(match.span(), match.group())
			self.str_resdict[match.span()]=match.group()
		
		# place this somewhere else later 
		self.strings_analysis()
