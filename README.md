usart-py
========

环境依赖：

   python2.7
   pyserial



文件说明
=============

* USART.py 封装串口屏基本命令

* extr.py 在基本命令基础上创建一些功能

* main.py 程序主文件，提供命令路由等功能

基本使用
=================

# 作为库使用：
<pre>
import USART

USART.connet("/dev/ttyS0",115200)  # 建立连接
USART.cls(2)                       # 进行各种操作
...
USART.ser.close() # 关闭


</pre>

usart-py 封装了USART的所有命令，调用方式为 *USART.* 命令的小写形式。
如 CLS(0） 被封装为 *USART.cls(0)*
 
所有的命令都有两个版本，  例如 *PS(x1,y1,x2,y2,c)* 被封装为 *USART.ps()*  和 *USART.aps()*
这两个函数功能完全一样，区别是，名称前面有 ‘a’ 的命令再调用后会自动输入 "\r\n" 字符串，
屏幕将马上显示绘制内容。而没有 'a' 作为前缀的版本，则需要输入"\r\n" 内容或者调用 USART.end()来
手动键入 "\r\n" 内容，让屏幕显示绘制的内容。

特殊的函数 cmd() 和 acmd（） 。它是一个通用性的函数，你可以用USART.cmd("命令") 来手动输入所有的USART屏幕的
命令


# 直接调用

*注意修改main.py文件中的 tty 变量，填写你系统上的TTL设备的路径 如 /dev/ttyS0*

*根据屏幕的分辨率修改USART.py文件中的 width和high两个变量的值。默认为 220 和 175*

<pre>

在终端下，运行

./main cmd "CLS(0) ;"   # 不需要手动加 \r\n ,因为默认这种情况下是立即进行绘图的。还可以输入任何其他命令。
./main pushinfo         # 将系统的运行信息显示在串口屏上






</pre>
