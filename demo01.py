'''
print("hello world!")
print("哈哈哈")
print(2333)
print(2.333)
print(True)
print(())#元组
print([])#数组
print({})#字典



print("哈哈哈",2333,2.333)#print，可以同时打印很多个值，用逗号隔开
print("哈哈哈"+"嘻嘻嘻")#字符串的拼接（只能同类型）  字符串+字符串
print("哈哈哈"*100)#打印100个‘哈哈哈’
print(((1+2)*100-99)/2)#可以用来做数学运算
print(((1+2)*100-9.9)/2)#整数和小数可以一起用来做数学运算
print(2>3)#布尔值false
print(2<3)#布尔值true



#变量（必须是小写字母，不能是特殊字符）
#赋值
a="张三" #把“张三”这个值赋值给了名字叫“a”的这个变量
print(a)



'''



'''
# a=input() #把input获取的输入的值存到a这个变量中
# print("input获取的内容:",a)

# a = input("请输入:") #把input获取的输入的值存到a这个变量中
# print("input获取的内容:",a)

a = input("请输入:") 
b = input("请输入:")#把input获取的输入的值存到a这个变量中
print("input获取的内容:",a+b)


#数据格式的转换 
print(type("哈哈哈"))#str字符串
print(type(2333))#int整数
print(type(2.333))#float小数
print(type(True))#bool布尔
print(type(()))#tuple元组
print(type([]))#list数组
print(type({}))#dict字典
'''



'''
#数据转换的规律：任何数据都可以转换为字符串，除了空值；整数和小数可以互相转换；字符串转换为其它类型的数据，必须【长得像
a = int("一")
print(type(a))
a = int("哈哈哈")
print(type(a))#################错误类型

a = int("2333")#字符串“”转换为整数
print(type(a))

a = str(2333)#整数转换为字符串
print(type(a))
'''


############实现加法的运算
# a = float(input("请输入:")) 
# b = float(input("请输入:"))#把input获取的输入的值存到a这个变量中
# print("input获取的内容:",a+b)

#len只支持字符串，元组，数组，字典，其余的不支持
# a = 'fajdfalsjdgiarodfkjljaslkdjf'
# print(len(a))

'''
练习：通过代码获取两段内容，并且计算他们的长度的和
'''
a = input("请输入第一段内容:") 
b = input("请输入第二段内容:")
print ("长度是:",len(a+b))