# -*- coding=utf-8 -*-

#发送测试结果到邮箱
import sys
sys.path.append("..")
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

def femail(self,receiver='',mail_title='',mail_content=''):
	host_server = 'smtp.qq.com'
	sender_qq_mail = '123456789@qq.com'
	smtp = SMTP_SSL(host_server)
	smtp.set_debuglevel(1)
	smtp.ehlo(host_server)
	smtp.login('123456789','asdasdasd')
	msg = MIMEText(mail_content,'plain','utf-8')
	msg['Subject'] = Header(mail_title + 'UI自动化测试报告','utf-8')
	msg['From'] = sender_qq_mail
	msg['To'] = receiver
	smtp.sendmail(sender_qq_mail,receiver,msg.as_string())
	smtp.quit()

class Email(object):
	def __init__(self):
		pass

	def send_mail(self,receiver = [],mail_title='',mail_content=''):
		a = ['123456789@qq.com']
		receiver = receiver + a
		for i in receiver:
			host_server = 'smtp.qq.com'
			sender_qq_mail = '123456@qq.com'
			smtp = SMTP_SSL(host_server)
			smtp.set_debuglevel(0)
			smtp.ehlo(host_server)
			smtp.login('123456','asdasdqwekjqwe')
			msg = MIMEText(mail_content,'plain','utf-8')
			msg['Subject'] = Header(mail_title + 'UI自动化测试报告','utf-8')
			msg['From'] = sender_qq_mail
			msg['To'] = i
			smtp.sendmail(sender_qq_mail,i,msg.as_string())
			smtp.quit()

if __name__ == '__main__':
	b = ['123456789@qq.com']
	Email().send_mail(b,mail_title='www.525j.com.cn',mail_content='测试通过')

