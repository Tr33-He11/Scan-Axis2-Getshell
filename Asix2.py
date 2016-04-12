#coding=utf-8
import requests
import threading
import time
import os
'''
AXIS2-扫描！
auther:weiyi（唯一）

'''
def check(i,total):
	global eu
	#os.system("title Spider,Current threads: %d,URLs left: %d,URLs exists:%d" %(threading.active_count(),total,eu)) 
	try:
		r = requests.get(i+'/axis2-web/index.jsp',timeout=10) #延时时间根据网速来定义
		status=r.content.count('Administration') #更改标题中所含的关键字
	except:
		print i,'Timeout' 
		status = 0
	if  status !=0: #通过标题判断
		r = 0
		print i,'Exists!!'
		eu+=1
		f = open("success.txt", 'a')
		f.write(i+'\n')
		f.close()
		
def main():
	global eu
	eu = 0
	total=len(open('url.txt','rU').readlines())
	print 'Total URLs:%d' %total
	for i in open("url.txt").readlines():
		i=i.strip('\n')
		t=threading.Thread(target=check, args=(i,total))
		t.setDaemon(True)
		total-=1
		while True:
			if(threading.active_count() == 1 and total == 0 ):
				print 'All Done at %s' %time.strftime("%Y-%m-%d[%H.%M.%S]")
				break
			elif (threading.active_count() < 200):
				if (total == 0):
					time.sleep(10) #10秒之后回到上一个if判断线程是否全部结束
				else:
					os.system("title Spider,Current threads: %d,URLs left: %d,URLs exists:%d" %(threading.active_count(),total,eu))
					t.start() #加载该线程
					break


if __name__ == '__main__':
	main()
