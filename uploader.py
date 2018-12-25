#!/usr/bin/python
#-*-coding:utf-8-*-
try:
	from dropbox import *
	import pathlib
	import sys
	import subprocess as a
	import os
	from time import sleep as mlor
except:
	print 'Install Module!'
	os.system('pip2 install dropbox')
	print 'Module Dropbox Terinstall'
	os.system('pip2 install pathlib')
	print 'Module Pathlib Terinstall';sys.exit()
class load:
	def __init__(self):
		b = ['...', '-', '/', '-', '/', '...']
		for c in b:
			print '\r[!]Load For Uploaded'+c,;sys.stdout.flush();mlor(0.4)
class Fack():
	def __init__(self, *args):
		try:
			self.fel = pathlib.Path('.')
			self.name = filee
			self.filepath = self.fel / self.name
			self.trgt = '/'
			self.target = self.trgt + self.name
		except:
			print 'File Tidak Ada Di Direktory'
			sys.exit()
	def tok(self):
		try:
			load()
			self.dp = Dropbox('6PxQa1ni6yAAAAAAAAAAC2mmfKav49ipywkKmmn_EanijpfvqrfD02tB7GxeyrA4')
			with self.filepath.open('rb') as b:
				meta = self.dp.files_upload(b.read(), self.target,
				mode = dropbox.files.WriteMode('overwrite'))
			self.link = self.dp.sharing_create_shared_link(self.target)
			print
			print '\n[=]Link :\n {}'.format(self.link.url)
			self.res = open('result.txt', 'w')
			self.res.write(self.link.url)
			self.res.close()
		except IOError:
			print '\n[!]File Tidak Di Temukan!'
			sys.exit()
if __name__=='__main__':
	a.call('clear', shell=True)
	baner = '''    _---------------(DropBox File Uploader)---------------_
\t\t        Author : Agung
\t\t     Team : AeX407, CRABS
    -_______________(DropBox File Uploader)_______________-
'''
	print baner
	filee = raw_input('[F]ile[U]ploader : ')
	kelas = Fack()
	kelas2 = kelas.tok()
	kelas2