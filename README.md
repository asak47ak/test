#WEB UI 自动化

基于python2.7 

chrome需要提前下载 chromedriver.exe 

firefox下载 geckodriver.exe

ie下载 IEDriverServer.exe

下载好后放在浏览器exe文件夹下

因为数据库涉及公司信息就没有放目录结构和数据库脚本上来

目录结构：

├─action.py 执行开始脚本
├─case 用例目录
├─component 组件目录
├─config 配置目录
├─report 报告目录
├─shotscreen 截图目录
└─src 方法目录
    ├─method.py
    ├─······
    └─log.py

流程：
输入action.py pramas1: pramas2 pramas3 pramas4 开始逐一执行case目录下的测试脚本，
一个case脚本一个数据库表，写入测试用例，执行结果，执行时间等信息，
每一个脚本执行完，写入测试套件执行记录表，通过与否，日期时间，用例数量，通过数量等，
全部执行完成后写入测试结果表，生成测试报告，上传测试报告。
