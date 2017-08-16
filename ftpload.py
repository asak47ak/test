# -*- coding=utf-8 -*-

import sys
import os
import json
from ftplib import FTP
  
_XFER_FILE = 'FILE'  
_XFER_DIR = 'DIR'  
  
class Xfer(object):  
    ''''' 
    @note: upload local file or dirs recursively to ftp server 
    '''  
    def __init__(self):  
        self.ftp = None  
      
    def __del__(self):  
        pass  
      
    def setFtpParams(self, ip, uname, pwd, port = 21, timeout = 60):          
        self.ip = ip  
        self.uname = uname
        self.pwd = pwd  
        self.port = port  
        self.timeout = timeout  
      
    def initEnv(self):  
        if self.ftp is None:  
            self.ftp = FTP()
            print '### connect ftp server: %s ...'%self.ip
            self.ftp.connect(self.ip, self.port, self.timeout)
            self.ftp.login(self.uname, self.pwd)
            print self.ftp.getwelcome()  
      
    def clearEnv(self):  
        if self.ftp:  
            self.ftp.close()  
            print '### disconnect ftp server: %s!'%self.ip   
            self.ftp = None  
      
    def uploadDir(self, localdir='./', remotedir='./'):  
        if not os.path.isdir(localdir):    
            return
        self.ftp.cwd(remotedir)   
        for file in os.listdir(localdir):  
            src = os.path.join(localdir, file)  
            if os.path.isfile(src):  
                self.uploadFile(src, file)  
            elif os.path.isdir(src):  
                try:    
                    self.ftp.mkd(file)    
                except:    
                    sys.stderr.write('the dir is exists %s'%file)  
                self.uploadDir(src, file)  
        self.ftp.cwd('..')
      
    def uploadFile(self, localpath, remotepath='./'):
        if not os.path.isfile(localpath):    
            return  
        print '+++ upload %s to %s:%s'%(localpath, self.ip, remotepath)
        self.ftp.storbinary('STOR ' + remotepath, open(localpath, 'rb'))
      
    def __filetype(self, src):  
        if os.path.isfile(src):  
            index = src.rfind('\\')  
            if index == -1:
                index = src.rfind('/')                  
            return _XFER_FILE, src[index+1:]  
        elif os.path.isdir(src):  
            return _XFER_DIR, ''          
      
    def upload(self, src):  
        filetype, filename = self.__filetype(src)
        self.initEnv()  
        if filetype == _XFER_DIR:  
            self.srcDir = src              
            self.uploadDir(self.srcDir)  
        elif filetype == _XFER_FILE:
            self.uploadFile(src, filename)
        self.clearEnv()

# def ftp_up(filename):
#     ftp=FTP()
#     ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
#     ftp.connect('192.168.1.241','21')#连接
#     ftp.login('123','123')#登录，如果匿名登录则用空串代替即可 
#     #print ftp.getwelcome()#显示ftp服务器欢迎信息
#     #ftp.cwd('xxx/xxx/') #选择操作目录
#     bufsize = 1024#设置缓冲块大小
#     file_handler = open(filename,'rb')#以读模式在本地打开文件 
#     ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件
#     ftp.set_debuglevel(0)
#     file_handler.close()
#     ftp.quit()
#     print "ftp up OK"

# if __name__ == '__main__':
#     srcDir = r"D:\autotest\TestCase\525j.com.cn\525j.com.cn v1.0.4\20170626184639"
#     srcFile = r'D:\autotest\TestCase\525j.com.cn\525j.com.cn v1.0.4\action.py'
#     xfer = Xfer()
#     xfer.setFtpParams('192.168.1.241', '123', '123')
#     xfer.upload(srcDir)
#     xfer.upload(srcFile)
