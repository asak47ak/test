# -*- coding=utf-8 -*-
import os
import sys
import time
import json
import datainsert
from ftplib import FTP

# reload(sys)
# sys.setdefaultencoding('utf-8')

class ReportCreat(object):
	def __init__(self,dist,date,version,result):
		self.dist = dist
		self.date = date
		self.version = version
		self.result = result
		self.upname = None

	__casestr = ''
	__fileas = None

	def havefile(self,file):
		return os.path.isfile(file)

	def createfile(self,text):
		res = None
		filename = ''
		filed = 'report/' + self.date + u'页面自动化测试v' + self.version + '.html'
		pfiled = 'report/'+self.date+u'页面自动化测试v'+self.version+'(PASS)' + '.html'
		ffiled = 'report/'+self.date+u'页面自动化测试v'+self.version+'(FAIL)' + '.html'
		if not self.havefile(pfiled) and not self.havefile(ffiled) and not self.havefile(filed):
			res = open(filed, 'w+')
			filename = filed
		else:
			namelis = filed.split('.')#提取为3部分
			li0 = namelis[0]#.前半部分
			li1 = namelis[1]#.中半部分
			li1lis = namelis[1].split('(')#中部分提取为2部分
			li2 = namelis[2]#.后半部分
			n = 1#增加的数量
			while self.havefile(li0 + '.' + str(int(li1lis[0]) + n) + '.' + li2) or self.havefile(li0 + '.' + str(int(li1lis[0]) + n) + '(PASS)' + '.' + li2) or self.havefile(li0 + '.' + str(int(li1lis[0]) + n) + '(FAIL)' + '.' + li2):
				n += 1
			res = open(li0 + '.' + str(int(li1lis[0]) + n) + '.' + li2, 'w+')
			filename = li0 + '.' + str(int(li1lis[0]) + n) + '.' + li2
		# res = open('D:/xampp/htdocs/index.html','w+')
		res.write(text)
		res.close()
		namelis = filename.split('.')
		os.rename(filename,namelis[0] + '.' + namelis[1] + '(' + self.result + ')' + '.' + namelis[2])
		self.upname = namelis[0] + '.' + namelis[1] + '(' + self.result + ')' + '.' + namelis[2]

	def creat(self):
		self.createfile('<!DOCTYPE html>\
			<html lang="zh-cn">\
				<head>\
					<meta charset="UTF-8">\
					<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scale=no">\
					<meta name="Author" content="golden">\
					<script src="../lib/vue.js"></script>\
					<script src="../lib/echarts.js"></script>\
					<script src="../lib/lightense.js"></script>\
					<link rel="stylesheet" href="../lib/dist/css/bootstrap.min.css">\
					<title>测试报告</title>\
					</head>\
					<style>\
						html {\
						    font-size : 20px;\
						}\
						@media (min-width: 401px){\
						    html {\
						        font-size: 25px !important;\
						    }\
						}\
						@media (min-width: 428px){\
						    html {\
						        font-size: 26.75px !important;\
						    }\
						}\
						@media (min-width: 481px){\
						    html {\
						        font-size: 30px !important; \
						    }\
						}\
						@media (min-width: 569px){\
						    html {\
						        font-size: 35px !important; \
						    }\
						}\
						@media (min-width: 641px){\
						    html {\
						        font-size: 40px !important; \
						    }\
						}\
						html,body{\
						    width: 100%;\
						}\
						.height{\
							height: 280px;\
						}\
						.da{\
							font-size: 60px !important;\
						}\
						.zhong{\
							font-size: 30px !important;\
						}\
						.text-demand{\
							margin-bottom: 60px;\
							line-height: 28px;\
							letter-spacing: 2px;\
						}\
						.text-ind{\
							text-indent: 2em;\
						}\
						.title{\
							clear: both;\
						}\
						.testcase1-a{\
							width: 20em;\
							float: left;\
						}\
						.testcase1-b{\
							float: left;\
						}\
						.testcase1-c{\
							float: right;\
						}\
						#demo{\
							height: 10rem;\
						}\
						.ltr{\
							width: 8rem;\
						}\
						.problemlist{\
						}\
						.problemlist .probone{\
							float: left;\
							margin-right: 15px;\
							transition: all .2s;\
						}\
						.probone > div{\
							width: 550px;\
						}\
						.proboneo{\
						}\
						.proboner img{\
							display: block;\
							width: 13rem;\
						}\
						ins{\
							cursor: pointer;\
						}\
					</style>\
				<body>\
					<div class="container">\
						<div class="clearfix">\
							<h1 class="page-header text-center da">{{projectname}}测试报告</h1>\
							<h3 class="text-center">（UI自动化）</h3>\
							<h3 class="text-center">版本：{{version}}</h3>\
							<h2 class="text-center">By：{{personnel}}</h2>\
							<div class="height"></div>\
							<address class="pull-right">\
								<strong>文件号：</strong><span>{{fnumber}}</span><br>\
								<strong>部门：</strong><span>技术测试部</span><br>\
								<strong>测试人员：</strong><span>{{personnel}}</span><br>\
								<strong>审核人员：</strong><span>戴金林</span><br>\
								<strong>时间：</strong><span>{{date}}</span><br>\
							</address>\
						</div>\
						<div class="row">\
							<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-tag"></span>  测试需求</h3>\
								<div class="text-demand text-justify">\
									<p class="text-ind">1.针对主页WWW.525J.COM.CN，UI自动化测试，为了更新迭代版本，快速响应，便于冒烟测试和手工测试，为开展功能自动化测试提供一个高效、稳定、容易的测试实现。</p>\
									<p class="text-ind">2.自动化测试能很好的利用资源在周未/晚上能够按计划自动的运行，合理利用有限的时间，这样充分的利用了公司的资源，也避免了开发和测试之间的等待。</p>\
									<p class="text-ind">3.增加软件信任度，只有经过大量测试案例测试过的版本才是可靠的，而只有使用自动测试才能够保证在段时间内完成大量的测试案例。</p>\
								</div>\
							</div>\
							<br>\
							<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-tasks"></span>  测试用例</h3>\
								<div class="list-group">\
									<div class="list-group-item testcase1" v-for="(item,index) in items">\
										<div class="title" @click="hide(item,index)">\
											<div class="testcase1-a">\
												<kbd>{{index + 1}}</kbd>\
												<span>{{item.case}}</span>\
											</div>\
											<div class="testcase1-b">\
												<span class="text-info">套件：{{item.suitename}}</span>\
												<small class="text-primary">总数：{{item.zi.length}}</small>\
												<small class="text-success">通过：{{len(item.zi,\'pass\')}}</small>\
												<small class="text-warning">跳过：{{len(item.zi,\'skip\')}}</small>\
												<small class="text-danger">失败：{{len(item.zi,\'failed\')}}</small>\
											</div>\
											<div class="testcase1-c">\
												<span class="caret" v-show="item.zi && item.zi.length"></span>\
												<span class="label label-success tpass" v-if="item.result == \'pass\'">通过</span>\
												<span class="label label-warning tskip" v-if="item.result == \'skip\'">跳过</span>\
												<span class="label label-danger tfailed" v-if="item.result == \'failed\'">失败</span>\
											</div>\
											<span class="clearfix"></span>\
										</div>\
										<div class="list-group" v-show="item.showed">\
											<div class="list-group-item testcase2" v-for="(it,ind) in item.zi">\
												<code>case{{ind + 1}}</code>\
												<span>{{it.case}}</span>\
												<div class="pull-right">\
													<span class="caret" v-show="it.zi && it.zi.length"></span>\
													<span class="label label-success cpass" v-if="it.result == \'pass\'">通过</span>\
													<span class="label label-warning cskip" v-if="it.result == \'skip\'">跳过</span>\
													<span class="label label-danger cfailed" v-if="it.result == \'failed\'">失败</span> <ins v-if="it.result == \'failed\'" v-on:click="towhere(it.suite,it.id)">详细</ins>\
												</div>\
											</div>\
										</div>\
									</div>\
								</div>\
							</div>\
							<br>\
							<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-file"></span>  脚本目录</h3>\
								<pre class="Catalog">\
{{projectname}}<br>\
	│  action.py 开始执行自动化测试脚本<br>\
	│  auditfile.txt 检查页面信息内容保存的文件<br>\
	│  data.json 生成测试报告的配置格式文件<br>\
	│  geckodriver.log firefox生成的log<br>\
	│  log.log 执行测试用例后生成的log<br>\
	│  readme.txt 测试前需要阅读的文件<br>\
	│  TestCase.xls 测试用例执行结果<br>\
	│  __init__.py <br>\
	│  目录结构.docx <br>\
	├─case 测试用例目录 <br>\
	│  │  case1.py 测试用例1<br>\
	│  │  ······ <br>\
	│  │  case26.py 测试用例26<br>\
	│  │  __init__.py <br>\
	├─component 组件目录 <br>\
	│      ClassModel.py <br>\
	│      placeorder.py <br>\
	│      print.py <br>\
	│      template.py <br>\
	├─config 配置文件目录<br>\
	│      id.txt 唯一ID <br>\
	│      url.txt 网址和浏览器 <br>\
	├─report 测试报告目录 <br>\
	│  │  20170606页面自动化测试v1.1.html 测试报告 <br>\
	│  │  ······ <br>\
	│  │  20170628页面自动化测试v1.0(PASS).html 测试报告 <br>\
	├─shotscreen 截图目录 <br>\
	│      ***.jpg <br>\
	└─src 框架目录<br>\
	    │  data.py 数据库配置<br>\
	    │  datainsert.py 数据库插入调用<br>\
	    │  dataquery.py 数据库查询调用<br>\
	    │  ftpload.py FTP上传脚本<br>\
	    │  generate.py 读取生成修改excel<br>\
	    │  img.py 截图和加文字<br>\
	    │  isfile.py 判断文件和文件路径<br>\
	    │  log.py 打印和保存log<br>\
	    │  main.py 启动浏览器<br>\
	    │  method.py 调用方法<br>\
	    │  msyh.ttf 字体<br>\
	    │  presentation.py 生成报告<br>\
	    │  sendEmail.py 发送邮件<br>\
	    │  wait.py 等待<br>\
	    │  __init__.py <br>\
	    └─report <br>\
								</pre>\
							</div>\
							<br>\
							<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-lock"></span>  测试结果</h3>\
								<table class="table table-bordered table-condensed">\
									<thead>\
										<tr>\
											<th></th>\
											<th>通过</th>\
											<th>跳过</th>\
											<th>失败</th>\
											<th>总数</th>\
											<th>通过率</th>\
											<th>结果</th>\
										</tr>\
									</thead>\
									<tbody>\
										<tr>\
											<td>测试套件：</td>\
											<td>{{tpass}}</td>\
											<td>{{tskip}}</td>\
											<td>{{tfailed}}</td>\
											<td>{{tpass + tskip + tfailed}}</td>\
											<td>{{((parseFloat(tpass / (tpass + tskip + tfailed))*100)).toFixed(2).toString()+"%"}}</td>\
											<td>--</td>\
										</tr>\
										<tr>\
											<td>测试用例：</td>\
											<td class="tg">{{cpass}}</td>\
											<td class="sk">{{cskip}}</td>\
											<td class="sb">{{cfailed}}</td>\
											<td>{{cpass + cfailed}}</td>\
											<td>{{((parseFloat(cpass / (cpass + cskip + cfailed))*100)).toFixed(2).toString()+"%"}}</td>\
											<td>\
												<span class="res" v-if="tg"><strong class="text-success">通过</strong></span>\
												<span class="res" v-if="!tg"><strong class="text-danger">不通过</strong></span>\
											</td>\
										</tr>\
										<tr>\
											<td>总计：</td>\
											<td></td>\
											<td></td>\
											<td></td>\
											<td>{{tpass + tskip + tfailed + cpass + cfailed}}</td>\
											<td></td>\
											<td></td>\
										</tr>\
									</tbody>\
								</table>\
							</div>\
							<div class="col-md-12">\
								<div class="col-md-5">\
									<div class="text-demand">\
										<div class="startend">测试开始时间：{{stime}} 测试结束时间：{{etime}}</div>\
										<div class="taking">耗时：{{taking}}</div>\
										<div class="time">测试日期：{{date}}</div>\
										<div class="grouped">唯一标识：{{grouped}}</div>\
										<div class="groupedmd5">唯一标识MD5：{{groupedmd5}}</div>\
										<div class="res" v-if="tg">测试结果：本次测试用例通过率为：{{((parseFloat(cpass / (cpass + cskip + cfailed))*100)).toFixed(2).toString()+"%"}}，大于98%，<strong class="text-success">测试通过</strong></div>\
										<div class="res" v-if="!tg">测试结果：本次测试用例通过率为：{{((parseFloat(cpass / (cpass + cskip + cfailed))*100)).toFixed(2).toString()+"%"}}，小于98%，<strong class="text-danger">测试不通过</strong></div>\
									</div>\
								</div>\
								<div class="col-md-7">\
									<div id="demo"></div>\
								</div>\
							</div>\
							<div class="col-md-12 problem">\
								<h3><span class="glyphicon glyphicon-warning-sign"></span>  问题汇总</h3>\
								<div classs="text-demand">\
									<div class="problemlist">\
										<div class="probone list-group" v-for="(sc,index) in screens">\
											<div class="proboneo list-group-item" v-bind:id="sc.suitename + sc.id"><b>标题</b> {{sc.suitename}}</div>\
											<div class="probonet list-group-item"><b>内容</b> {{sc.text}}</div>\
											<div class="proboner list-group-item"><img class="imgs" v-bind:src="sc.grouped + \'/\' + sc.src" alt="screen" v-on:click="showImg(sc.grouped + \'/\' + sc.src)"></div>\
											<div class="probonef list-group-item"><b>日志</b> <a v-bind:href="sc.grouped + \'/log.log\'" target="_blank">LOG</a></div>\
										</div>\
										<div class="clearfix"></div>\
									</div>\
								</div>\
							</div>\
							<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-paperclip"></span>  附件</h3>\
								<div classs="text-demand">\
									{{annex}}\
									<a v-bind:href="grouped + \'/auditfile.txt\'" target="_blank">数据</a>\
								</div>\
							</div>\
							<!--<div class="col-md-12">\
								<h3><span class="glyphicon glyphicon-book"></span>  测试总结</h3>\
								<div class="text-demand">\
									{{explain}}\
								</div>\
							</div>-->\
							<address class="text-center">\
								<small> 我爱我家网 上海鸿洋电子商务股份有限公司</small>\
							</address>\
						</div>\
					</div>\
					<script>\
						var vm = new Vue({\
							el:".container",\
							data:{\
								items:'+json.dumps(self.dist['testcase'])+',\
								screens:'+json.dumps(self.dist['screenshot'])+',\
								projectname:"'+self.dist['projectname']+'",\
								describe:"'+self.dist['describe']+'",\
								version:"'+self.dist['version']+'",\
								platform:"'+self.dist['platform']+'",\
								Browser:"'+self.dist['Browser']+'",\
								language:"'+self.dist['language']+'",\
								tools:"'+self.dist['tools']+'",\
								method:"'+self.dist['method']+'",\
								demand:"'+self.dist['demand']+'",\
								expect:"'+self.dist['expect']+'",\
								personnel:"'+self.dist['personnel']+'",\
								date:"'+self.dist['date']+'",\
								explain:"'+self.dist['explain']+'",\
								taking:"'+self.dist['taking']+'",\
								stime:"'+self.dist['stime']+'",\
								etime:"'+self.dist['etime']+'",\
								fnumber:"'+self.dist['fnumber']+'",\
								grouped:"'+self.dist['grouped']+'",\
								groupedmd5:"'+self.dist['groupedmd5']+'",\
								annex:"'+self.dist['annex']+'",\
								tg:false,\
								tpass:0,\
								tskip:0,\
								tfailed:0,\
								cpass:0,\
								cskip:0,\
								cfailed:0,\
								cnotdo:0\
							},\
							mounted:function(){\
								this.$nextTick(function(){\
									this.demo()\
								})\
							},\
							methods:{\
								hide:function(item,index){\
									if(typeof item.showed == "undefined"){\
										this.$set(item,"showed",true);\
									}else{\
										item.showed = !item.showed;\
									}\
								},\
								demo:function(){\
									this.tpass = document.getElementsByClassName("tpass").length;\
									this.tskip = document.getElementsByClassName("tskip").length;\
									this.tfailed = document.getElementsByClassName("tfailed").length;\
									this.cpass = document.getElementsByClassName("cpass").length;\
									this.cskip = document.getElementsByClassName("cskip").length;\
									this.cfailed = document.getElementsByClassName("cfailed").length;\
									var all = document.getElementsByClassName("label").length;\
									var testcase1 = document.getElementsByClassName("testcase1").length;\
									var testcase2 = document.getElementsByClassName("testcase2").length;\
									this.tg = (this.cpass / (this.cpass + this.cskip + this.cfailed)) > 0.98;\
								},\
								len:function(obj,res){\
									var count = 0;\
									for(var i = 0; i < obj.length; i++){\
										if(obj[i].result == res){\
											count += 1;\
										}\
									}\
									return count;\
								},\
								towhere:function(suit,ind){\
									var tow = document.getElementById(suit+ind).parentNode;\
									var sTop = document.body.offsetTop;\
									var problem = document.getElementsByClassName("problem")[0];\
									window.scrollTo(0,problem.offsetTop - 50 + tow.offsetTop - sTop);\
									setTimeout(function(){tow.style.boxShadow = "4px 4px 50px #c01920";},500);\
									setTimeout(function(){tow.style.boxShadow = "none";},1500);\
								},\
								showImg:function(ele){\
									console.log(ele);\
								}\
							}\
						});\
					</script>\
					<script>\
						setTimeout(function(){\
							var mychart = echarts.init(document.getElementById("demo"));\
							var tg = Number(document.getElementsByClassName("tg")[0].innerHTML);\
							var sk = Number(document.getElementsByClassName("sk")[0].innerHTML);\
							var sb = Number(document.getElementsByClassName("sb")[0].innerHTML);\
							var option = {\
							    title : {\
							        text: "测试用例通过率",\
							        subtext: "UI自动化",\
							        x:"center"\
							    },\
							    tooltip : {\
							        trigger: "item",\
							        formatter: "{b} : {c} ({d}%)"\
							    },\
							    legend: {\
							        orient: "vertical",\
							        top: "30%",\
							        left: "10%",\
							        data: ["通过","跳过","失败","错误"]\
							    },\
							    series : [\
							        {\
							            name: "",\
							            type: "pie",\
							            radius : "45%",\
							            center: ["50%", "60%"],\
							            data:[\
							                {value:tg, name:"通过",itemStyle:{normal:{color:"#abc123"}}},\
							                {value:sk, name:"跳过",itemStyle:{normal:{color:"#373e40"}}},\
							                {value:sb, name:"失败",itemStyle:{normal:{color:"#f17c67"}}},\
							                {value:0, name:"错误",itemStyle:{normal:{color:"#654321"}}}\
							            ],\
							            itemStyle: {\
							                emphasis: {\
							                    shadowBlur: 20,\
							                    shadowOffsetX: 2,\
							                    shadowColor: "rgba(0, 0, 0, 0.5)"\
							                }\
							            }\
							        }\
							    ]\
							};\
				        	mychart.setOption(option);\
							var el = document.querySelectorAll(".imgs");\
							Lightense(el);\
						},2000)\
					</script>\
				</body>\
			</html>')
		return self.upname.split('/')[1]

# if __name__ == '__main__':
# 	file= open('../data.json','r+')
# 	cal = file.read()
# 	file.close()
# 	dist = eval(cal)
# 	print (ReportCreat(dist,time.strftime("%Y%m%d", time.localtime()),'1.0','FAIL').creat()).encode('UTF-8')


