# -*- coding=utf-8 -*-
import os
import time
import sys
import random

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#给图片加上文字
class images(object):
	def __init__(self,imageUrl,content):
		self.imageUrl = imageUrl
		self.content = content

	def imageRes(self):
		im = Image.open(self.imageUrl)
		w,h=im.size
		print w,h
		dImg=im.resize((w/2,h/2),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
		dImg.save(self.imageUrl)

	def imageEdit(self):
		font = ImageFont.truetype("C:\Windows\Fonts\simhei.ttf",25)
		im = Image.open(self.imageUrl)
		draw = ImageDraw.Draw(im)
		text = unicode(self.content,'UTF-8')
		draw.text((0,100), text, font=font, fill=(0,250,154,0))
		im.save(self.imageUrl)

if __name__ == '__main__':
	# images('../shotscreen/123.png','http://www.525j.com.cn').imageRes()
	images('../shotscreen/123.jpg','http://www.525j.com.cn').imageEdit()
