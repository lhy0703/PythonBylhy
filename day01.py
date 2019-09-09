a = int(input('请输入'))
print(a,type(a))
  #进行格式化输出
a = input('请输入')
b = input('请输入')
print('%.2f - %.2f = %.2f'%(a,b,a-b))
print('%.3f + %.3f = %.3f'%(a,b,a+b))
print('%.2f * %.2f = %.2f'%(a,b,a*b))
print('%.2f / %.2f = %.2f'%(a,b,a/b))
    #类型转化
 #a = 100
 #b = str(a)
 #print(b,type(b))
      #进行比较
#a = 200
#b = 200
#print(a is b)
#a = True
#print(not a)
      #进行加密
# email = '666@qq.com'
#for e in email:
#   o = ord(e) - 10
#  print(chr(o),end="") 
      #md5加密
#import hashlib
#a = input('请输入字符串：')
#hashlib.md5(a.encode(encoding = 'UTF-8')).hexdigest()
       #闰年
#year = int(input('请输入年份:>>'))
#if (year%4==0 and year % 100 !=0) or (year %400 ==0):
#   print('%d 是一个闰年'%year)
#else:
#   print('%d 不是闰年'%year)
        #水仙花数
#num = input('请输入一个三位数:')
#bai = int(num[0])
#shi = int(num[1])
#ge = int(num[2])
#  if bai ** 3 +shi ** 3 + ge ** 3 == int(num):
#    print('这个数为水仙花数')
#  else:
#    print('这个数不是水仙花数')
       #华氏温度转换摄氏温度
# f = float(input('请输入华氏温度:'))
#c = (f - 32)/1.8
#print('转化后的摄氏温度为:%.2f'%c)
       #每个月的天数
#year = input(('请输入一个月份:'))
#a =['1','3','5','7','8','10','12']
#b =['4','6','9','11']
#c =['2']
#if year in a:
#  print('此月有31天')
#elif year in b:
#  print('此月有30天')
#else:
#  print('此月有28天')
        #温度转化
#C = float(input('请输入摄氏温度:'))
#F = (9 / 5) * C + 32
#print('转化后的华氏温度：%.2f'%F)
       #圆柱的体积与面积
#r = float(input('请输入半径:'))
#h = float(input('请输入高:'))
#pai = 3.1415926535
#area = r * r * pai
#volume = area * h
#print('area = %.4f'%area)
#print('volume = %.4f'%volume)
        #英尺与米的转换
#feet = float(input('Enter length the feet:'))
#meter = 0.305 * feet
#print('%.4f meters'%meter)
       #计算能量
#M = float(input('Enter kilograms:'))
#initialtemp = float(input('Enter initial temp:'))
#finaltemp = float(input('Enter final temp:'))
#Q = M * (finaltemp - initialtemp) * 4184
#print('所需的能量：%.4f'%Q)
       #计算利息
#Blance = float(input('Please Enter Blance:'))
#IR = float(input('Please Enter Interest rate:'))
#I = Blance * (IR/1200)
#print('The interest is:%.5f'%I)
        #加速度
#v0 = float(input('Please Enter v0:'))
#v1 = float(input('Please Enter v1:'))
#t = float(input('Please Enter use time:'))
#a = (v1 - v0)/t
#print('平均加速度为：%.4f'%a)
         #复利值
#num = float(input('请输入每月存款数:'))
#rate = 0.05/12
#interest = 1 + rate
#count = [0]
#for i in range(6):
#month = (100 + count[i]) * interest
#count.append(month)
#print('六个月后的账户总额:%.2f'%count[6])
        #整数中的各位数字求和
num = int(input('输入1-1000之间的整数:'))
bai = int(num//100)
shi = int(num//10%10)
ge = int(num%10)
sum = bai + shi +ge 
print('The sum of the is:',sum)
