    #一个五边形的面积
# import math
# r = float(input('r='))
# pai = 3.14
# s = 2*r*math.sin(pai/5)
# area = 5*s*s/(4*math.tan(pai/5))
# print('The area of the pentagon is:%.2f'%area)




   #大圆距离
# import math
# x1,y1 = input('请输入第一个点的经纬度:').split(',')
# x2,y2 = input('请输入第二个点的经纬度:').split(',')
# x1_1 = math.radians(float(x1))
# y1_1 = math.radians(float(y1))
# x2_2 = math.radians(float(x2))
# y2_2 = math.radians(float(y2))
# radians = 6371.01
# d = radians*math.acos(math.sin(x1_1)*math.sin(x2_2) + math.cos(x1_1)*math.cos(x2_2) * math.cos(y1_1 - y2_2))
# print('大圆的距离是:%.5f'%d)


   #五角星的面积
# import math
# side = float(input('Enter the side:'))
# Area = 5*side**2/(4*math.tan( math.pi/5))
# print('The area of the pentagon is:%.4f'%Area)






    #一个正多边形的面积
# import math
# sides = float(input('Enter the number os sides:'))
# side = float(input('Enter the side:'))
# Area = sides *side**2 /(4*math.tan(math.pi/sides))
# print('The area of the polygon is:%.4f'%Area)





    #找出ASCII码的字符
# a = int(input('Enter an ASCII code:'))
# print(chr(a))




     #工资表
# username = input('Enter employee`s name:')
# work_h = input('Enter number of hours worked in a week:')
# hours_p = input('Enter hourly pay rate:')
# Gross_pay = input('Enter federal tax withholding rate:')
# state = input('Enter state tax withholding rate:')
# print('Employee Name:' +username)
# print('Hours worked:%2f(float(work_h))')
# print('Pay Rate:$' +str(hours_p))
# print('Gross Pay:$'+str(work_h*hours_p))
# print('Deductions:\nFederal Withholding(20.0%):$'+str(work_h*hours_p*0.2)+'\n  State Withholding(9.0%):  $'+
#          str(work_h*hours_p*0.09)+'\nTotal Deduction:$%.2f'%((work_h*hours_p*0.2)+(work_h*hours_p*0.09)))
# print('Net Pay:$%.2f'%(((work_h*hours_p)-((work_h*hours_p*0.2)+(work_h*hours_p*0.09)))))






    #反向数字
# a = input('Enter an integer:')
# print(a[::-1])



   #文本加密
# import hashlib
# m = hashlib.md5()
# a = input('请输入加密文本:')
# m.update(bytes(a,encoding='UTF-8'))
# with open('passwd.txt','w')as file:
#     file.write(m.hexdigest())
# print(m.hexdigest())


############################################################




    #1.解一元二次方程
# import math
# a = input('请输入a=')
# b = input('请输入b=')
# c = input('请输入c=')
# panbie = (float(b)*float(b))-(4*float(a)*float(c))
# if panbie >0:
#     x1 = (-float(b)+math.sqrt(panbie))/2*float(a)
#     x2 = (-float(b)-math.sqrt(panbie))/2*float(a)
#     print('The roots are %.6f and %.6f'%(x1,x2))
# elif panbie == 0:
#     x1 = (-float(b)+math.sqrt(panbie))/2*float(a)
#     print('The root is %.2f'%(x1))
# else:
#     print('The equation has no real roots')




   #2.学习加法
# import random
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)
# sum = input('请输入猜测的数字')
# if sum == num1 + num2:
#     print('true')
# else:
#     print('false')




   #3.找未来数据
# d = int(input('Enter today`s day:'))
# num = int(input('Enter the number of days elapsed since today:'))
# d_list =['Sunday','Monday','Tuesday','Wednesday','Thursday','Firday','Saturday']
# sum_= d + num
# zhou = sum_%7
# print('Today is:'+d_list[d]+'and the future day is '+ d_list[zhou])




   #4.对三个整数排序
# a = input('a=')
# b = input('b=')
# c = input('c=')
# d = [a,b,c]
# d.sort()
# print(d)




   #5.比较价钱
# weight1,price1 = input('请输入第一种包装的重量与价格:').split(',') 
# weight2,price2 = input('请输入第二种包装的重量与价格:').split(',')
# package1 = float(price1)/float(weight1)
# package2 = float(price2)/float(weight2)
# if package1 < package2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')





   #6.找出一月中的天数
# year = input('请输入年:')
# mouth = input('请输入月份:')
# list_mouth1 = ['1','3','5','7','8','10','12']
# list_mouth2 = ['4','6','9','11']
# if int(year)%4 == 0:
#     if mouth in list_mouth1:
#         print(year+'\000年\000'+mouth+'月有31天。')
#     elif mouth in list_mouth2:
#         print(year+'\000年\000'+mouth+'月有30天。')
#     else:
#         print(year+'\000年\000'+mouth+'月有29天。')
# else:
#     if mouth in list_mouth1:
#         print(year+'\000年\000'+mouth+'月有31天。')
#     elif mouth in list_mouth2:
#         print(year+'\000年\000'+mouth+'月有30天。')
#     else:
#         print(year+'\000年\000'+mouth+'月有28天。')






   #7.头或尾
# import random
# a = random.choice(['正','反'])
# b = input('请用户输入猜测值:')
# if b == a:
#     print('true')
# else:
#     print('false')





   #8.石头，剪刀，布
# import numpy as np
# computer = np.random.choice(['0','1','2'])
# User = input('用户输入 [剪刀(0) /石头(1) /布(2)]:')
# if (computer == User):
#     print('平局')
# elif (computer == '0' and User == '布'):
#     print('你输了')
# elif (computer == '1' and User == '剪刀'):
#     print('你输了')
# elif (computer == '2' and User == '石头'):
#     print('你输了')
# else:
#     print('你赢了')





   #9.一周的星期几
# year = int(input('请输入年:'))
# m = int(input('请输入月:'))
# d = int(input('请输入天:'))
# week = ['周日','周一','周二','周三','周四','周五','周六']
# h = int(d + ((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
# day = week[h]
# if m == 1:
#     m = 13
#     year = year -1
# if m == 2:
#     m = 14
#     year = year -1  
# print('那一天是一周中的:%s'%day)




   #10.选出一张牌
# import random
# num = ['1','2','3','4','5','6','7','8','9','10','jack','queen','king']
# huase = ['♣','♥','♦','♠']
# choice1 = random.choice(['1','2','3','4','5','6','7','8','9','10','jack','queen','king'])
# choice2 = random.choice(['♣','♥','♦','♠'])
# print('The card you picked is the ' + choice1  + '\000of\000' + choice2)





   #11.回文数
# num = input('Eenter a three-digit integer num=:')
# a = num[::-1]
# if a == num:
#     print('num is a palindrome')
# else:
#     print('num is not a palindrome')




     #12.计算三角形的周长
# a,b,c = input('Enter three edges:').split(',')
# a = float(a)
# b = float(b)
# c = float(c)
# if a + b >c and a + c > b and b + c >a:
#     L = a + b + c 
#     print('周长为L')
# else:
#     print('输入错误')





##############################################################
   #1.正负数
   #2.计算未来学费
# money = 10000
# sum1 = 0
# for i in range (1,14):
#     money = money * 0.05 + money 
#     if i == 10:
#         print('十年之后的学费：%2.f'%money)
#     if i >= 10:
#         sum1 +=money
# print('十年后大学四年的总学费为:%.2f'%sum1) 
# 
# 
# 
# 
# 
#  
    #4.被5、6同时除的数
# geshu = 0
# for i in range(100,1001):
#     if i%5 == 0 and i%6 == 0:
#         geshu += 1
#         print(i,end='\t')
# print()


    #8.数列求和
# sum = 0
# for i in range (3,100,2):
#     sum += (i - 2)/i
# print('数列的和为:',sum)




    #9.计算π
# pi =0
# i = int(input('请输入i的值:'))
# for j in range(1,i+1):
#     pi +=4*((-1)**(1+j)/(2*j-1))
# print('π的值为：%f'%pi) 



    #10.完全数
for i in range(1,10000):
    x = 0
    for j in range(1,i):
        if i %j ==0:
            x += j
    if x ==i:
        print('10000一下的完全数有:%d'%x)
