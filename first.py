#/usr/bin/python3
#pyrhon中的字符串用单引号或双引号括起来，同时使用反斜杠\转义特殊字符
#变量[头下表:尾下标]
str='Runoob'
print(str)#输出字符串
print(str[0:-1])#输出第一个到倒数第二个字符串
print(str[0])#输出字符串第一个字符
print(str[2:5])# 输出从第三个开始到第五个的字符
print(str[2:])#输出从第三个开始后的所有字符
print(str*2)#输出字符串两次，也可以写成print(2*str)
print(str+"TEST")#连接字符串
print('Ru\noob')
print(r'Ru\noob')
#另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。 
word='Python'
print(word[0],word[5])#第一个和最后一个
print(word[-1],word[-6])#倒数第一个和倒数最后一个
