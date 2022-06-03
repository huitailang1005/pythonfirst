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
#!/usr/bin/python3
	#元组
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
print("==============================")
