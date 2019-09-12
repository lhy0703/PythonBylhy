    #1.五角星
# COUNT = 0
# def getPentagonalNumber(n):
#     global COUNT
#     for i in range(1,n+1):
#         num = n *(3*i - 1)/2
#         print("%d"%num,end=' ')
#         COUNT += 1
#         if COUNT %10 == 0:
#             print('\n')
# getPentagonalNumber(100)




     #2.求一个整数各个数字的和
# word = input('请输入整数：')
# j = len(word)
# list_num = []
# def main1(word):
#     global j
#     global list_num
#     for i in range(len(word)):
#         a=int(word)%10
#         word = str(int(word)//10)
#         list_num.append(a)
#         j -= 1
#         if j==0:
#             sum_ = sum(list_num)
#             print(sum_)

# main1(word)





   #3.对整数进行排序
# def displaySortedNumbers(a,b,c):
#     # a = input('a=')
#     # b = input('b=')
#     # c = input('c=')
#     d = [a,b,c]
#     d.sort()
#     print(d)
# displaySortedNumbers(3,5,1)




     #5.显示字符
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=' ')
#         if i %10 == 0:
#             print('\n')
# printChars()


    #6.一年的天数
# def numberOfDayInYear(year):
#     for i in range(year,year+11):
#         if (i %4 == 0 and i %100 != 0) or (i %100 == 0 and i %400 == 0):
#             print('{}年有366天'.format(i))
#         else:
#             print('{}年有365天'.format(i))
# numberOfDayInYear(2010)



     #7.显示角
# def distance (x1,y1,x2,y2):
#     dis =((x1 - x2)**2 + (y1 - y2)**2)**0.5
#     print("距离为:%f"%dis)
# distance(1,4,4,2)




    #当前日期和时间
import time
def main():
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
main()




    #掷骰子
# import random
# def touzhi():
#     a = random.choice(['1','2','3','4','5','6'])
#     b = random.choice(['1','2','3','4','5','6'])
#     if (a + b) == 2 or (a + b) == 3 or (a + b) == 12:
#         print('%d + %d = %d'%(a,b,a+b))
#         print('你输了')
#     elif (a + b) == 7 or (a + b) == 11:
#         print('%d + %d = %d'%(a,b,a+b))
#         print('你赢了')
#     else:
#         print('%d + %d = %d'%(a,b,a+b)) 
#         c = random.choice(['1','2','3','4','5','6'])
#         d = random.choice(['1','2','3','4','5','6'])
#         if (c + d) == 7:
#             print('%d + %d = %d'%(c,d,c+d)) 
#             print('你输了')
#         elif (c + d) == (a + b):
#             print('%d + %d = %d'%(c,d,c+d))
#             print('你赢了')
# touzhi()
    



