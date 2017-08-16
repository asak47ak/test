# -*- coding:utf-8 -*-

import selenium
from selenium import webdriver
import os
import time
import sys
sys.path.append("..")
from src import main
from src import wait
from src import data
from src import img
from src import dataquery
from src import datainsert
from src import generate
from src import method

#切换地区
def start():
	stime = time.time()
	sheetname = u'case_changecity'
	gen = generate.ExcelEdit()
	onlyid = gen.readtxt('./config/id.txt',0)
	print 'CASE1 ------START------'

	url = gen.readtxt('./config/url.txt',0)
	explore = gen.readtxt('./config/url.txt',1)
	wait.PublicTimeSleep('\n\n\nCASE1测试开始').onlyLog()
	driver = None

	try:
		wait.PublicTimeSleep('使用浏览器：' + explore).onlyLog()
		driver = main.Driver(url,explore).doit()
		wait.PublicTimeSleep('打开浏览器并进入' + url).onlyLog()
		dr = method.find(driver,sheetname)
		dr.max()
		dr.setVal('id','city',u'上海')
		dr.setClick('css','input[value="搜索"]')
		dr.cururl()

		'''
		start
		'''
		dr.checkResult(dr.setClick('css','#city .closed strong'),u'点击切换城市按钮，弹出选择你的城市。')
		dr.checkResult(dr.setClick('a','北京'),u'点击热门城市北京')
		dr.contrastResult(dr.cururl(),'http://www.525j.com.cn/beijing/','页面跳转到http://www.525j.com.cn/beijing/')

		dr.checkResult(dr.setClick('css','#city .closed strong'),u'点击切换城市按钮，弹出选择你的城市。')
		dr.checkResult(dr.setClick('a','常州'),u'点击热门城市常州')
		dr.contrastResult(dr.cururl(),'http://www.525j.com.cn/changzhou/','页面跳转到http://www.525j.com.cn/changzhou/')

		dr.checkResult(dr.setClick('css','#city .closed strong'),u'点击切换城市按钮，弹出选择你的城市。')
		dr.checkResult(dr.setClick('a','金华'),u'点击热门城市金华')
		dr.contrastResult(dr.cururl(),'http://www.525j.com.cn/jinhua/','页面跳转到http://www.525j.com.cn/jinhua/')

		dr.checkResult(dr.setClick('css','#city .closed strong'),u'点击切换城市按钮，弹出选择你的城市。')
		dr.checkResult(dr.setClick('a','苏州'),u'点击热门城市苏州')
		dr.contrastResult(dr.cururl(),'http://www.525j.com.cn/suzhou/','页面跳转到http://www.525j.com.cn/suzhou/')

		'''
		end
		'''
		
		etime = time.time()
		alltime = etime - stime
		dotime = time.strftime("%Y%m%d", time.localtime())
		allc = datainsert.StartInsert().querycasecount(sheetname,onlyid)
		pc = datainsert.StartInsert().querycasepcount(sheetname,onlyid)
		fc = datainsert.StartInsert().querycasefcount(sheetname,onlyid)
		datainsert.StartInsert().insertMain(u'切换地区','y','','x',str(alltime),dotime,onlyid,sheetname,onlyid,allc,pc,fc)
		wait.PublicTimeSleep('CASE1测试结束，测试通过').onlyLog()
	except:
		dr.insertdb(u'页面报错',u'failed',dr.screenShot())

		etime = time.time()
		alltime = etime - stime
		dotime = time.strftime("%Y%m%d", time.localtime())
		allc = datainsert.StartInsert().querycasecount(sheetname,onlyid)
		pc = datainsert.StartInsert().querycasepcount(sheetname,onlyid)
		fc = datainsert.StartInsert().querycasefcount(sheetname,onlyid)
		datainsert.StartInsert().insertMain(u'切换地区','x','','y',str(alltime),dotime,onlyid,sheetname,onlyid,allc,pc,fc)
		wait.PublicTimeSleep('CASE1脚本运行出错，测试失败').onlyLog()
	finally:
		dr.delcookies()
		dr.quite()
	
	print '\n\n\nCASE1 ------OVER------'

if __name__ == '__main__':
	start()
