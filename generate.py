# -*- coding=utf-8 -*-
#结果生成

import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
import datainsert

# wb = xlrd.open_workbook(u'../测试用例.xlsx')
# sh = wb.sheet_by_index(0)

# print sh

# for i in range(sh.nrows):
# 	print sh.row_values(i)

# print sh.cell(0,0).value
# print sh.cell(rowx=0,colx=1).value


# rb = xlrd.open_workbook(u'../TestCase.xls')
# wb = copy(rb)
# ws = wb.get_sheet(0)
# ws.write(1,1,'change2')
# wb.save(u'../TestCase.xls')

'''
parms1 文件路径和文件名
parms2 excel的sheet index
parms3 行
parms4 列
parms5 内容
'''
class ExcelEdit(object):
	def __init__(self):
		pass

	def edit(self,file,sheetname,row,col,text):
		self.workbook = xlrd.open_workbook(file)
		self.indexx = self.workbook.sheets().index(self.workbook.sheet_by_name(sheetname))
		self.workbookcopy = copy(self.workbook)
		self.workbookcopy.encoding = 'utf-8'
		self.sheetindex = self.workbookcopy.get_sheet(self.indexx)
		self.sheetindex.write(row,col,text)
		self.workbookcopy.save(file)


	def create(self,file,sheetname,row,col,value):
		self.biao = xlwt.Workbook(file)
		self.table = self.biao.add_sheet(sheetname)
		self.table.write(row,col,value)
		self.biao.save(file)

	def addsheets(self,file,sheetname):
		try:
			self.workbook = xlrd.open_workbook(file)
			self.workbookcopy = copy(self.workbook)
			self.workbookcopy.encoding = 'utf-8'
			self.workbookcopy.add_sheet('%s' % sheetname,cell_overwrite_ok=True)
			self.workbookcopy.save(file)
		except:
			return False			

	def read(self,file,index,row,col):
		self.excel = xlrd.open_workbook(file)
		self.table = self.excel.sheets()[index]
		return self.table.cell(row,col).value

	def changesheetname(self):
		pass

	def readtxt(self,file,ind):
		fb = open(file,'r')
		lines = fb.readlines()
		fb.close()
		return str(lines[ind].strip('\n')).lower()


# if __name__ == '__main__':
	# wr = ExcelEdit()
	# wr.edit('./TestCase.xls',u'用例',0,0,u'测试用例')
	# print wr.read('./TestCase.xls',0,0,0)
	# wr.addsheets('./TestCase.xls',u'用例2')
	# print wr.readtxt('log.log',0)

