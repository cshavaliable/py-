#1 字符串判断
#1.1 startswich():是否以某个字符为开头，是的话返回True，不是则返回False，如果设置开始和结束位置则只在此位置内查找
#startswith("子字符串",首位,末位)
# st = "河北宁晋"
# print(st.startswith("河"))
# print(st.startswith("北",1,3))
from gettext import find

# 1.2endswith 是否以某个字符为结尾，是的话返回True，不是则返回False，如果设置开始和结束位置则只在此位置内查找
# 与startswith同理

# 1.3 isupper():检测字符串中是否都为大写，是的话返回True
# st = "nnjy"
# print(st.isupper())
# print(st.islower())
# print(st.upper())
# str.upper()：把所有字母转成大写（注意：不是判断，是转换）。
#
# str.lower()：把所有字母转成小写。
#
# str.isalpha()：判断是否全是字母。
#
# str.isdigit()：判断是否全是数字。
#
# str.isspace()：判断是否全是空白字符（空格、换行等）

# 2 修改元素
# 2.1 replace():替换
# replace(旧内容，新内容，替换次数)
# replace默认替换所有
# name = "好好学习，天天向上"
# print(name.replace("好","美"))
# print(name.replace("天","日",1))

#2.2 split 指定分隔符来分割字符串
# st = "hello,python"
# print(st.split(",")) #输出结果 ['hello', 'python']
# print(st.split("o")) #输出 ['hell', ',pyth', 'n']
# print(st.split("v")) #若是字符串中不包含该分隔符,就返回整体
# print(st.split("o",1))#可指定次数

#2.3 capitalize():第一个元素大写
# st = "hehe"
# print(st.capitalize())

# 2.4 lower 全改为小写
#
# 2.5 upper 全改为大写
# 此用法与capitalize都相同


#3 列表
#基本格式
#列表名 = [元素1,元素2,元素3]
#注意元素之间用,隔开,元素类型可以不相同
# li = [1,2,3,4]
# # 列表也可以进行for循环
# print(li[1:3])

#3.1 列表基本操作
#append() extend() insert() 均为添加
# li = ["one","two","three"]
# li.append("four")
 #append() 添加整体
# li.extend("four")
# print(li)
# 而extend是将字符拆分为单个元素
# insert 需要下标:指定位置添加
# li.insert(3,"four")
# print(li)

#3.2 修改列表元素'
#直接通过下标就可以进行修改
# li = [1,2,3]
# li[1] = "a"
# print(li)

#3.3 查找元素
# in: 判断元素是否在字符里,如果是则返回True ,如果无则返回False
# not in: 判断元素是否在字符里,如果无则返回True ,如果有则返回False
# li = ['a','b','c','d','e','f']
# print("e"in li)
# print("k"in li)
# print("k"not in li )
#count 和 index 都是查找
# li = ['a','b','c','d','e','f']
# print(li.index("a",0,1))
# print(li.count("b"))

#3.4删除元素
#3.4.1 del #默认删除所有
# li = [3,4,5,6]
#del li #删除列表
# del li[1] #删除下标所在的元素
# print(li)

#3.4.2pop 默认删除最后一个 也可用下标来删除
# li.pop(1)
# print(li)

# 3.4.3 remove:根据元素来删除
# li.remove(3)
# li.remove(8)
# print(li)
#若是没找到则会报错

#3.5 排列
#3.5.1 sort 按照从小到大的顺序排列
# li = [3,7,6,5,8]
# li.sort()
# print(li)
# #3.5.2 reverse: 倒序，将列表反过来
# li.sort(reverse=True)
# print(li)

#3.6 列表推导式
#格式一：[表达式 for 变量 in 列表]
#注意:in 后面不止可以放列表，还可以放range()、可迭代对象
# [print(i) for i in range(1,6)]
# li = []
# [li.append(i) for i in range(1,6)]
# print(li)
# 两式等价
# for i in range(1,6):
#     li.append(i)
# print(li)

#格式二：[表达式 for 变量 in 列表 if 条件]
# for i in range (1,11):
#     if i % 2 == 1:
#         print(i)
# for i in range (1,11):
#     if i % 2 == 0:
#         print(i)
# li = []
# [li.append(i) for i in range(1, 11) if i % 2 == 1]
# print(li)

#3.7 列表嵌套
# li = [1,2,3,[4,5,6]] #[4,5,6]为里面的列表 与1，2，3 并列为单个子字符串
# print(li[3])  #取出[4，5，6]
# print(li[3][0]) #取出4
