# -*- coding:utf-8 -*-

import os
import time
import sys
import random
import logging

####以后修改文件名和行号
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='log.log',
                filemode='a+')

class delFile(object):
	def __init__(self,fname):
		self.name = fname

	def rmFile(self):
		os.remove(self.name)

	def rmFolder(self):
		os.rmdir()

	def rmFolders(self):
		os.removedirs()

#delFile('log.log').rmFile()

class openFileAndRead(object):
	def __init__(self,txt):
		#写入log的内容
		self.txt = txt
		#log生成的详细时间
		self.nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	def creatFile(self):
		self.file = open('auditfile.txt','a+')

	def writeFile(self,txt):
		# self.file.write(self.nowtime + ' ' + self.txt +'\n')
		self.file.write(self.txt +'\n')

	def closeFile(self):
		self.file.close()

	def doWrite(self):
		self.creatFile()
		self.writeFile(self.txt)
		self.closeFile()

	def readWrite(self):
		logging.info(self.txt.encode('gbk'))

if __name__ == '__main__':
	# openFileAndRead(str(100)).readWrite()
	# openFileAndRead('阿三的哈捷克苏丹海军可阿三大家金卡和').readWrite()
	openFileAndRead(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'谁知盘中餐粒粒皆asdasd123132132辛苦'+str(65451515)).doWrite()


