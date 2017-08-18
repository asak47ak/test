##WEB UI 自动化

基于python2.7 

chrome需要提前下载 chromedriver.exe 

firefox下载 geckodriver.exe

ie下载 IEDriverServer.exe

下载好后放在浏览器exe文件夹下

因为数据库涉及公司信息就没有放数据库脚本上来，主要脚本都有。

目录结构：

<pre>
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
</pre>

流程：

输入action.py pramas1: pramas2 pramas3 pramas4 开始逐一执行case目录下的测试脚本，

一个case脚本一个数据库表，写入测试用例，执行结果，执行时间等信息，

每一个脚本执行完，写入测试套件执行记录表，通过与否，日期时间，用例数量，通过数量等，

全部执行完成后写入测试结果表，生成测试报告，上传测试报告，发送测试结果邮件。

细节：

用xampp apache弄了个python cgi的服务器，可以通过web页面执行单个或全部的测试用例，然后在结果里查看所有的记录，再查看每次的测试报告。
用到了前端的VUE框架，确实好用！

执行全部用例需要花费4个小时多，手机会收到18条预定短信，所以就在每天下班18：00开始自动执行，用windows的计划任务。

执行完所有的脚本后会给目标邮件发送测试结果邮件

不足：

对于数据库的结构的冗余需要再提升
容错率需要提升
脚本维护成本较高
其它...
