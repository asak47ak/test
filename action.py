# -*- coding=utf-8 -*-
import os
import shutil
import time
import xlrd
import sys
import simplejson
import case
import json
from src import ftpload
from src import log
from src import presentation
from src import generate
from src import datainsert
from src import sendEmail
from ftplib import FTP

reload(sys)
sys.setdefaultencoding('utf-8')

class Action(object):
	def __init__(self):
		self.onlyone = None
		self.stime = None
		self.stimem = None
		self.etimem = None
		self.etime = None
		self.resultd = None
		self.resul = None
		self.disk = None
		self.ratesum = None
		self.filename = ''

	def __call__(self):
		pass

	def onlyid(self,ids='native'):
		#写当前执行的唯一标识
		self.onlyone = ''
		if ids == 'native':
			self.onlyone = time.strftime("%Y%m%d%H%M%S", time.localtime())
			ff = open('./config/id.txt','w+')
			ff.write(self.onlyone)
			ff.close()
		else:
			self.onlyone = str(ids)
		return self.onlyone

	def Getlen(self,dir,ext = None):
		allfiles = []
		needExtFilter = (ext != None)
		for root,dirs,files in os.walk(dir):
			for filespath in files:
				filepath = os.path.join(root, filespath)
				extension = os.path.splitext(filepath)[1][1:]
				if needExtFilter and extension in ext:
					allfiles.append(filepath)
				elif not needExtFilter:
					allfiles.append(filepath)
		return len(allfiles)

	def itv2time(self,iItv):
		if type(iItv) == type(1):
			h = iItv / 3600
			sUp_h = iItv - 3600 * h
			m = sUp_h / 60
			sUp_m = sUp_h - 60 * m
			s = sUp_m
			# return ":".join(map(str,(h,m,s)))
			return str(h) + "小时" + str(m) + "分" + str(s) + "秒"
		else:
			return "type error"

	def walk_dir(self,dir,topdown=True):
		fileList = []
		for root, dirs, files in os.walk(dir, topdown):
			for name in files:
				fileList.append(os.path.join(root,name))
		return fileList

	def copy_files_to_dir(self,dirSrc,dirDst):
		files = self.walk_dir(dirSrc)
		for f in files:
			ext = os.path.splitext(f)[1];
			b = f.split('n\\')
			shutil.copy2(f, os.path.join(dirDst,b[1]))

	def clear(self,browser):
		#把原来的log清空
		if(os.path.exists('./log.log')):
			f = open('./log.log','w+')
			f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
			f.close()

		#把原来的auditfile清空
		if(os.path.exists('./auditfile.txt')):
			f = open('./auditfile.txt','w+')
			f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
			f.close()

		#清空原来的shotscreen文件夹
		shutil.rmtree('./shotscreen')
		os.mkdir('shotscreen')

		#浏览器
		a = open('config/url.txt','w+')
		a.write('http://www.525j.com.cn/\n%s' % browser)
		a.close()

		#是否在测试中
		ac = open('config/action.txt','w+')
		ac.write('True')
		ac.close()

	def doit(self,sumone,conti=0):
		self.stime = time.strftime("%H时%M分%S秒", time.localtime())
		self.stimem = time.time()
		l = self.Getlen('case','.py')
		if sumone == 'all' and int(conti) == 0:
			for i in range(1,17):
				eval('case.case%s.start()' % i)
		elif sumone == 'all' and conti != 0 and type(conti) == int and conti > 0 and conti < l:
			for j in range(1,l):
				if j == conti:
					continue
				else:
					eval('case.case%s.start()' % j)
		elif int(sumone) > 0 and int(sumone) < l:
			eval('case.case%s.start()' % str(sumone))
		else:
			print 'arg error'
		self.etime = time.strftime("%H时%M分%S秒", time.localtime())
		self.etimem = time.time()

	def diskList(self,person):
		#读取data.json的配置 生成的字典结构
		file = open('./data.json','r+')
		cal = file.read()
		file.close()
		#把读取的内容转为字典
		self.disk = json.loads(cal)
		#执行人
		self.disk['personnel'] = person.decode('gbk')
		#报告日期
		self.disk['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		#文件号
		self.disk['fnumber'] = time.strftime("%Y%m%d", time.localtime())
		#用例耗时
		self.disk['taking'] = 0
		#读取数据库测试用例详细数据
		a = datainsert.StartInsert().querycase('main_table',self.onlyone)
		for ind,j in enumerate(a):
			if j[2] == 'y' and j[4] == 'x':
				self.disk['testcase'].append({'case':j[1].encode('utf-8'),'result':'pass','suitename':j[11],'zi':[]})
			elif j[2] == 'x' and j[4] == 'y':
				self.disk['testcase'].append({'case':j[1].encode('utf-8'),'result':'failed','suitename':j[11],'zi':[]})
			else:
				self.disk['testcase'].append({'case':j[1].encode('utf-8'),'result':'skip','suitename':j[11],'zi':[]})
			b = datainsert.StartInsert().querycase(j[11],self.onlyone)
			for index,i in enumerate(b):
				self.disk['testcase'][ind]['zi'].append({'case':i[1].encode('utf-8'),'result':i[2].encode('utf-8'),'id':i[0],'suite':j[11].encode('utf-8')})
			c = datainsert.StartInsert().queryFailCase(j[11],self.onlyone)
			for indexx,k in enumerate(c):
				self.disk['screenshot'].append({'id':k[0],'text':k[1].encode('utf-8'),'result':k[2].encode('utf-8'),'src':k[3].encode('utf-8'),'grouped':k[4].encode('utf-8'),'suitename':j[11].encode('utf-8')})
			self.disk['taking'] += float(j[5])
		#修改耗时格式
		self.disk['taking'] = self.itv2time(int(self.disk['taking']))
		#脚本结束时间
		self.etime = time.strftime("%H时%M分%S秒", time.localtime())
		self.etimem = time.time()
		self.disk['grouped'] = str(self.onlyone)
		self.disk['groupedmd5'] = str(datainsert.StartInsert().md5(str(self.onlyone)))
		self.disk['stime'] = str(self.stime)
		self.disk['etime'] = str(self.etime)
		
	def filecopyup(self,email):
		alltable = str(int(datainsert.StartInsert().querytablecount()) - 2)
		allsum = datainsert.StartInsert().queryallsum('main_table',self.onlyone)
		passsum = datainsert.StartInsert().querypsum('main_table',self.onlyone)
		failedsum = datainsert.StartInsert().queryfsum('main_table',self.onlyone)
		tasktimesum = datainsert.StartInsert().querytimesum('main_table',self.onlyone)
		self.ratesum = "%.3f" % (float(passsum)/float(allsum))
		if float(self.ratesum) > 0.98:
			self.resultd = 'pass'
			self.resul = 'PASS'
		else:
			self.resultd = 'failed'
			self.resul = 'FAIL'
		os.mkdir('D:/xampp/htdocs/report/' + str(self.onlyone))
		os.mkdir('D:/xampp/htdocs/report/' + str(self.onlyone)  + '/shotscreen')
		shutil.copy('./auditfile.txt','D:/xampp/htdocs/report/' + str(self.onlyone))
		shutil.copy('./log.log','D:/xampp/htdocs/report/' + str(self.onlyone))
		self.copy_files_to_dir('./shotscreen','D:/xampp/htdocs/report/' + str(self.onlyone) + '/shotscreen')
		self.filename = presentation.ReportCreat(self.disk,time.strftime("%Y%m%d", time.localtime()),str(self.disk['version']),self.resul).creat()
		# self.filename = presentation.ReportCreat(self.disk,str(20170721),str(self.disk['version']),self.resul).creat()
		shutil.copy('./report/'+self.filename,'D:/xampp/htdocs/report/')
		datainsert.StartInsert().insertResult(self.disk['projectname'],self.resultd,self.disk['etime'],str(self.ratesum),self.disk['version'],alltable,allsum,str(self.stimem),str(self.etimem),tasktimesum,self.disk['demand'],self.onlyone,'',self.onlyone,self.filename,self.disk['personnel'])
		sendEmail.Email().send_mail(email,self.disk['projectname'],str(self.disk['projectname'])+' '+str(self.resultd).upper()+' '+str(self.disk['date']))
		
		ac = open('config/action.txt','w+')
		ac.write('False')
		ac.close()

	def start(self,sumone='all',conti=0,person='测试部',browser='chrome',email=''):
		ac = open('config/action.txt','r+')
		acread = ac.read()
		ac.close()
		if acread == 'False':
			email = email.split('-')
			email = email[0:-1]
			self.clear(browser)
			self.onlyid()
			self.doit(sumone,conti)
			self.diskList(person)
			self.filecopyup(email)
		else:
			return False

if __name__ == '__main__':
	# Action().start(100,0,'测试部','chrome')
	if len(sys.argv) == 6:
		Action().start(str(sys.argv[1]),int(sys.argv[2]),sys.argv[3],str(sys.argv[4]),sys.argv[5])
	elif len(sys.argv) == 5:
		Action().start(str(sys.argv[1]),int(sys.argv[2]),sys.argv[3],str(sys.argv[4]),'')
	else:
		print 'argv error!'
