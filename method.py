# -*- coding=utf-8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import sys
import main
import log
import img
import generate
import wait
import datainsert

reload(sys)
sys.setdefaultencoding('utf-8')

def getScreen(f):
	def inner(a):
		try:
			f(a)
		except:
			a.driver.get_screenshot_as_file('./screenshot/'+str(time.time()) + '.jpg')
	return inner

class find(object):
	def __init__(self,driver,sheetname):
		self.driver = driver
		self.sheetname = sheetname

	def getEle(self,typed,ele):
		try:
			if typed == 'id':
				return self.driver.find_element_by_id(ele)
			elif typed == 'css':
				return self.driver.find_element_by_css_selector(ele)
			elif typed == 'a':
				return self.driver.find_element_by_link_text(ele)
			elif typed == 'xpath':
				return self.driver.find_element_by_xpath(ele)
			else:
				return False
		except:
			# self.insertdb(typed + u' 查找元素失败 ' + ele,u'failed',self.screenShot())
			return 'ele error'

	def findele(self,typed,ele):
		if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
			wait.PublicTimeSleep(typed + ele + ' 元素存在').time_sleep_sort()
			return True
		else:
			wait.PublicTimeSleep(typed + ele + ' 元素不存在').time_sleep_sort()
			return False
	
	def setClick(self,typed,ele,sleep='two'):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				self.getEle(typed,ele).click()
				if sleep == 'two':
					wait.PublicTimeSleep(typed + ' ' + ele + ' 点击元素').time_sleep_sort()
				else:
					wait.PublicTimeSleep(typed + ' ' + ele + ' 点击元素').time_sleep_sortt()
				return True
			else:
				return False
		except:
			# self.insertdb(typed + u' 点击元素 ' + ele,u'failed',self.screenShot())
			return 'ele error'

	def setVal(self,typed,ele,text):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				self.getEle(typed,ele).send_keys(text)
				wait.PublicTimeSleep(typed + ' ' + ele +' 输入内容：' + text).time_sleep_sort()
				return True
			else:
				return False
		except:
			# self.insertdb(typed + ' ' + ele + u' 输入内容： ' + text,u'failed','')
			return 'value error'

	def setClear(self,typed,ele):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				self.getEle(typed,ele).clear()
				wait.PublicTimeSleep(typed + ' ' + ele +' 清空内容').time_sleep_sort()
				return True
			else:
				return False
		except:
			# self.insertdb(u' 清空 '+ ele + u' 内容 ',u'failed','')
			return 'clear error'

	def moveOn(self,typed,ele):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				ActionChains(self.driver).move_to_element(self.getEle(typed,ele)).perform()
				wait.PublicTimeSleep(typed + ' 鼠标移入： ' + ele).time_sleep_sort()
				return True
			else:
				return False
		except:
			# self.insertdb(typed + u' 鼠标移入： '+ ele,u'failed','')
			return 'moveon error'

	def moveOffset(self,typed,ele,x,y):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				ActionChains(self.driver).move_to_element_with_offset(self.getEle(typed,ele),x,y).perform()
				wait.PublicTimeSleep(' 鼠标移到： ' + ele + ' ' + str(x) + ' ' + ' ' + str(y)).time_sleep_sort()
				return True
			else:
				return False
		except:
			# self.insertdb(u' 鼠标移到： '+ ele + ' ' + str(x) + ' ' + ' ' + str(y),u'failed','')
			return 'moveoffset error'

	def max(self):
		try:
			self.driver.maximize_window()
			wait.PublicTimeSleep('浏览器最大化').time_sleep_sort()
		except:
			return False

	def min(self):
		try:
			self.driver.set_window_size(960,1040)
			self.driver.set_window_position(0,0)
			wait.PublicTimeSleep('浏览器变化到960,1040 并移动到左上角').time_sleep_sort()
		except:
			return False

	def cururl(self):
		wait.PublicTimeSleep('浏览器当前url:' + self.driver.current_url).onlyLog()
		return self.driver.current_url

	def delcookies(self):
		try:
			self.driver.delete_all_cookies()
		except:
			# self.insertdb(u'为IE浏览器删除所有cookie',u'failed','')
			return False

	def changehand(self,num):
		try:
			self.driver.switch_to_window(self.driver.window_handles[num])
			wait.PublicTimeSleep('切换浏览器窗口句柄到'+str(num)).time_sleep_sort()
			return True
		except:
			# self.insertdb(typed + u' 切换浏览器窗口错误 ',u'failed',self.screenShot())
			wait.PublicTimeSleep('切换浏览器窗口错误').time_sleep_sort()
			return False

	def changeframe(self,name):
		try:
			self.driver.switch_to_frame(name)
			wait.PublicTimeSleep('切换窗口框架句柄到' + name).time_sleep_sort()
			return True
		except:
			# self.insertdb(typed + u' 切换窗口框架句柄错误 ',u'failed',self.screenShot())
			wait.PublicTimeSleep('切换窗口框架句错误').time_sleep_sort()
			return False

	def containtext(self,typed,ele,txt):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				if txt in self.getEle(typed,ele).text:
					return 'have'
				else:
					return 'exit'
			else:
				return False
		except:
			return 'containtext error'
			# self.insertdb(ele + u'元素是否包含：' + txt,u'failed','')

	def consoletext(self,typed,ele):
		try:
			if self.getEle(typed,ele) != 'ele error' and self.getEle(typed,ele) != False:
				txt = self.getEle(typed,ele).text
				wait.PublicTimeSleep(typed + ele + ' 元素内的文本：'+ txt).time_sleep_sort()
				return txt
			else:
				return False
		except:
			# self.insertdb(ele + u' 元素未找到：',u'failed',self.screenShot())
			return 'consoletext error'

	def getback(self):
		try:
			self.driver.back()
			wait.PublicTimeSleep('浏览器后退').time_sleep_sort()
			return True
		except:
			# self.insertdb(u' 浏览器后退',u'failed',self.screenShot())
			return False

	def close(self):
		try:
			self.driver.close()
			wait.PublicTimeSleep('关闭当前页').time_sleep_sort()
			return True
		except:
			# self.insertdb(u' 关闭当前页',u'failed',self.screenShot())
			return False

	def quite(self):
		try:
			self.driver.quit()
			wait.PublicTimeSleep('关闭浏览器').onlyLog()
			return True
		except:
			# self.insertdb(u' 关闭浏览器',u'failed','')
			return False

	def screenShot(self,txt='default'):
		try:
			imgurl = u'shotscreen/'+str(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))+'.jpg'
			self.driver.get_screenshot_as_file(imgurl)
			# img.images(imgurl,str(self.driver.current_url)).imageRes()
			if txt == 'default':
				img.images(imgurl,str(self.driver.current_url)).imageEdit()
			else:
				img.images(imgurl,str(self.driver.current_url)+ ' ' + str(txt)).imageEdit()
			wait.PublicTimeSleep('截图编辑并保存').time_sleep_sort()
			return imgurl
		except:
			# self.insertdb(u'截图失败',u'failed','')
			return False

	def executeJs(self,js):
		try:
			self.driver.execute_script(js)
			wait.PublicTimeSleep('执行javascript语句' + js).time_sleep_sort()
			return True
		except:
			# self.insertdb(u' 执行javascript语句' + js,u'failed',self.screenShot())
			return False

	def checkResult(self,f,t):
		if f == True:
			self.insertdb(t,'pass','')
		else:
			self.insertdb(t,'failed',self.screenShot(t))

	def contrastResult(self,f,r,t):
		if f == r:
			self.insertdb(t,'pass','')
		else:
			self.insertdb(t,'failed',self.screenShot(t))

	def insertdb(self,txt,result,storage):
		grouped = generate.ExcelEdit().readtxt('./config/id.txt',0)
		datainsert.StartInsert().insertCase(self.sheetname,txt,result,storage,grouped,grouped)
		
	# def insertdb(self,txt,result,storage):
	# 	pass

if __name__ == '__main__':
	ch = main.Driver('http://www.baidu.com','chrome')
	driver = ch.doit()
	dr = find(driver,u'case_changecity')
	dr.setVal('id','kw',u'肖申')
	dr.setClick('id','su')
	dr.findele('css','#kw')
	dr.setClear('id','kw')
	dr.setClick('id','su')
	dr.max()
	dr.containtext('css','#setf','百度一下')
	dr.min()
	dr.consoletext('id','setf')
	dr.getback()
	dr.quite()

# try:
# 	WebDriverWait(driver,10).until(lambda x: x.find_element_by_css_selector('#citys')).click()
# except:
# 	print 1
# wait.PublicTimeSleep().time_sleep()
