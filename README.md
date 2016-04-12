# Scan-Axis2-Getshell

Scan AXIS2 目录里是扫描ip及端口的、
利用s扫描器、这里S扫描器就自己找吧，免得说有后门！
Bat payload

@echo off
color 8e
mode con cols=50 lines=7
Title  Scan
cls&echo. 
color 8e
echo  开始扫描:
set /p port=请输入要扫描的端口 :
if not "%Choice%"=="" set Choice=%Choice:~0,1%
for /f "eol= tokens=1,2 delims= " %%i in (ip.txt) do s syn %%i %%j %Port% /save
for /f "eol=- tokens=1 delims= " %%i in (result.txt) do echo %%i>>s1.txt
for /f "eol=P tokens=1 delims= " %%i in (s1.txt) do echo %%i>>s2.txt
for /f "eol=S tokens=1 delims= " %%i in (s2.txt) do echo http://%%i:8090/axis2>>ips.txt
del result.txt
del s1.txt
del s2.txt 
