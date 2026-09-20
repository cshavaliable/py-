# a = "哈哈"
# b = "嘿嘿"
# if a == "哈哈" and b == "嘿嘿":
#     print("a是哈哈，b是嘿嘿。")
# # print( not 3>9)
# 1.2 三目运算 倒装句
# # a = 5
# # b = 9
# # print("a小于等于b") if a <= b else print("a大于b")

# 1.3 if - elif
# score = float(input("你的成绩是："))
# if   80 < score <= 100:
#     print("你的成绩为优秀")
# elif 60 < score <= 80:
#     print("你的成绩为良好")
# elif   0 < score <= 60:
#     print("你还仍需努力")
# else:
#     print('分数无效')
#
# 1.4 if嵌套
# ticket = True
# temp = 36.2
# if ticket ==True:
#     print('你可以进站了哈哈——》',end="")
#     if  36.2<= temp <= 37.2:
#         print("体温正常，可以上车")
#     else:
#         print('体温不正常，禁止上车')
# else:
#     print("你不可以进站")

# #2.1 while循环
# i = 1
# while i <= 10:
#     print('csh, nb')
#     i += 1
# #2.2 while死循环
# while True:
#     print('csh, nb')

# # 2.3 while 求和
# i = 1
# s = i
# while i < 100:
#     i += 1
#     s += i
# print(s)

# #2.4 while 内外循环
# i = 1
# while i <=3: #这是外循环
#     print(f'这是第{i}次外循环')
#     i += 1
#     j = 1
#     while j <=3:
#         print(f"这是第{j}次内循环")
#         j += 1

# 3 for 循环
#  3.1 基本格式 for 临时变量 in 可迭代对象:
#     循环体
#注意缩进和冒号

# str = "Hello World"
# for i in str:
#     print(i)

# 3.2 range()函数
# for i in range(3):
#     print('力量在于人民')

# 3.3 for循环利用
# s = 0
# # for i in range(1,101):
# #     s += i
# #     print(f"计算结果是{s}.")

# a = input("你的名字是")
# print(a)
# 3.4 break and  continue 用法
i = 1
# while i <= 5:
#     print(f"小明吃到了第{i}个苹果")
#     i += 1
#     if i == 3:
#         print("小明吃到了坏苹果不吃了")
#         i += 1
#         continue
# while i <= 5:
#     print(f"小美吃到了第{i}个苹果")
#     i += 1
#     if i == 3:
#         print(f"小美吃到了第{i}个苹果吃饱了不吃了")
#         break

# for i in range(6):
#     if i == 2:
#         break
#     print(i)

# 4,1 编码与解码
# a = "这里是五四广场"
# print(a,type(a))
# a1 = a.encode("unicode_escape")
# print(a1,type(a1))
# a2 = a1.decode("unicode_escape")
# print(a2,type(a2))

# b = "这里是五四广场"
# b1 = b.encode("utf-8")
# print(b1,type(b1))
# b2 = b1.decode("utf-8")
# print(b2,type(b2))

# 5 字符串常见操作
# 5.1 字符串拼接
# print(10+10)
# print("10"+"10")
# name1 = "曹"
# name2 = "世和"
# # print(name1 + name2)
# # print(name1 , name2)
#
# print(name1 , name2,sep="")
#
# print("hello world\r"*5)
# s = "hello world\r" * 5
# print(repr(s))

#5.2 成员运算符
# name = "曹世和"
# print("c" in name)
# print("曹和" in name )
# print("曹" in name)
#5.3 下标
# 作用: 快速找到对应的数据
# 注意：py中下标从0开始
#格式：字符串名+[]
# name = "曹世和"
# print(name[0])
# print(name[1])
# #从右往左数用 -1 开始
# print(name[-1])

#5.4 切片
#语法： [开始位置：结束位置：步长]
# 包前不包后
# kk = "kskblzdjd"
# # print(kk[0:5])
#
# #从右往左
# print(kk[:5])
# print(kk[-5:])
# print(kk[-1:])
# #默认从左往右切，若想从右往左切 需要改变步长
# print(kk[-1:-5:-1]) #改变方向
# print(kk[0:6:2]) #改变步长，一个过一个

# 字符串查找 依旧包前不包后
#6.1 find函数
name = "caoshihe"
# print(name.find("c"))
# print(name.find("h",3,4))

#6.2 index()函数
# index("子字符串",首位,末位)
# print(name.index("c"))
#index与find区别为： 找不到时index为报错，find为输出—1

#6.3 count()函数
#count("子字符串",首位,末位)
# name = "hehe0324"
# print(name.count("h",1))
#
# 三种索引函数均为包前不包后，但count函数为数数