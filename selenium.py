#! /usr/bin/env python
# -*- coding=utf-8 -*-
#3.20 golden 肖申

import selenium
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class Driver(object):
	__chrome = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	__ie = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
	driver = None #webdriver实例

	def __init__(self,url,typefind):
		self.url = url #要登录的地址
		self.typefind = typefind #要使用哪个浏览器

	def chromedriver(self):
		os.environ['webdriver.chrome.driver'] = self.__chrome
		self.driver = webdriver.Chrome(self.__chrome)
		self.driver.get(self.url)

	def ie(self):
		os.environ['webdriver.ie.driver'] = self.__ie
		self.driver = webdriver.Ie(self.__ie)
		self.driver.get(self.url)

	def firefox(self):
		self.driver = webdriver.Firefox()
		self.driver.get(self.url)

	def open(self):
		if self.typefind == 'chrome':
			self.chromedriver()
		elif self.typefind == 'ie':
			self.ie()
		elif self.typefind == 'firefox':
			self.firefox()
		elif self.typefind == 'all':
			self.chromedriver()
			self.ie()
			self.firefox()

	def doit(self):
		self.open()
		return self.driver #返回webdriver实例，以便让其它基本调用

# ch = Driver("file:///C:/Python27/python/test.html","chrome").doit()


# ch.save_screenshot('ele.jpg')

# time.sleep(1)

# nowhandle = ch.current_window_handle

# ch.find_element_by_css_selector(".openmodal").click()

# allhandles = ch.window_handles

# for handle in allhandles:
# 	print 1
# 	if handle != nowhandle:
# 		ch.switch_to_window(handle)
# 		ch.find_element_by_css_selector("button[class='btn btn-default']").click()
# 		print 2

# time.sleep(1)

# ch.switch_to_window(nowhandle)

# time.sleep(1)

# ch.find_element_by_css_selector("button[class='btn btn-default']").click()
