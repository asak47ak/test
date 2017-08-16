# -*- coding=utf-8 -*-

import time
import log
import generate

class PublicTimeSleep(object):
	def __init__(self,text='sleep'):
		self.text = text

	def time_sleep(self):
		if(self.text == 'sleep'):
			print 'active sleep time 5s...'
			log.openFileAndRead('active sleep time 5s...').readWrite()
		else:
			print self.text.decode('utf-8'),'active sleep time 5s...'
			log.openFileAndRead(self.text).readWrite()
		time.sleep(5)

	def time_sleep_sort(self):
		if(self.text == 'sleep'):
			print 'active sleep time 2s...'
			log.openFileAndRead('active sleep time 2s...').readWrite()
		else:
			print self.text.decode('utf-8'),'active sleep time 2s...'
			log.openFileAndRead(self.text).readWrite()
		time.sleep(2)

	def time_sleep_sortt(self):
		if(self.text == 'sleep'):
			print 'active sleep time 0.5s...'
			log.openFileAndRead('active sleep time 0.5s...').readWrite()
		else:
			print self.text.decode('utf-8'),'active sleep time 0.5s...'
			log.openFileAndRead(self.text).readWrite()
		time.sleep(0.5)

	def onlyLog(self):
		print self.text.decode('utf-8')
		log.openFileAndRead(self.text).readWrite()

if __name__ == '__main__':
	# PublicTimeSleep('合适的阿萨德阿斯撒').time_sleep()
	# PublicTimeSleep('合适的阿萨德阿斯撒').time_sleep_sort()
	# PublicTimeSleep('合适的阿萨德阿斯撒').time_sleep_sortt()
	PublicTimeSleep('合适的阿萨德阿斯撒').onlyLog()
