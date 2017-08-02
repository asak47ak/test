# -*- coding=utf-8 -*-
#基础浏览器配置

import selenium
import time
import os
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.opera import options

class Driver(object):
	__chrome = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	__ie = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
	__operaDriverLoc = os.path.abspath('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
	__operaExeLoc = os.path.abspath('D:\\opera\\46.0.2597.32\\opera.exe')
	
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

	def opera(self):
		__operaCaps = desired_capabilities.DesiredCapabilities.OPERA.copy()
		__operaOpts = options.ChromeOptions()
		__operaOpts._binary_location = self.__operaExeLoc
		self.driver = webdriver.Chrome(executable_path = self.__operaDriverLoc, chrome_options = __operaOpts, desired_capabilities = __operaCaps)
		self.driver.get(self.url)

	def open(self):
		if self.typefind == 'chrome':
			self.chromedriver()
		elif self.typefind == 'ie':
			self.ie()
		elif self.typefind == 'firefox':
			self.firefox()
		elif self.typefind == 'opera':
			self.opera()
		elif self.typefind == 'all':
			self.chromedriver()
			self.ie()
			self.firefox()
			self.opera()

	def doit(self):
		self.open()
		return self.driver #返回webdriver实例，以便让其它脚本调用

if __name__ == '__main__':
	Driver('http://www.baidu.com','opera').doit()
