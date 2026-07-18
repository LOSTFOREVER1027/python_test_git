# #just for fun
# list1=[9,8,7,6,5,4,3,2,1,0]
# list1.reverse()
# print(list1)

# list2=list1[0:5]
# print(list2)

# for i in list2:
#     print(i)
#     print('i')
#     print("i")



# # format
# print("{0} love {1} . {2}".format('I','my','com'))
# print('{a} love {b} . {c}'.format(a='I',b='me',c='!'))
# print('%c'%97)

# print('%c%c%c%c%c' % (70,105,115,104,67))

# print('%d 10 is %o 8' % (1027,1027))

# print('%d in kexue is %e' % (1027,1027))

# str1='一支穿云箭，千军万马来相见；'
# str2='两幅忠义胆，刀山火海提命现。'

# print('%s%s' % (str1,str2))

# print('a\'')
# print('a\"')
# print('\"a\"')
# print('1\n')
# print('2\t3')
# print('3\v4')

# print('5\r')
# print('6\f')


# #
# a=list()
# print(a)

# b=list('love')
# print(b)

# c=list((0,1,2,3,4,5))
# print(c)

# print(max(list1))

# print(min(list1))

# print(sum(list1))

# print(list1,list1.sort(),list1)

# print(list1)

# list2=list1.sort()

# print(list2)

# list1=[9,8,7,6,5,4,3,2,1,0]
# list2=list1[:]
# print(list1)
# print(list2)

# list1.sort()

# print(list1)

# sorted(list2)

# print(list2)
# print(sorted(list2))

# def myfunction():
#     print('it is my first function')
#     print('i \'d like to say sth.')
#     print('thanks to cctv tvb\n')

# print(myfunction())

# def function_sin(x):
#     print((x))

# print(function_sin(2))

# def add(num1,num2):
#     return num1+num2
# print(add(1,2))

# #lambda

# g=lambda x:2*x+1
# print(g(5))

# g= lambda x,y:x+y
# print(g(1,2))

# def funX(x):
#     return lambda y:x*y

# temp=funX(8)
# print(temp(5))

# #filter

# temp=filter(None,[1,0,False,True])
# print(list(temp))

# def odd(x):
#     return x%2

# temp = filter(odd,range(10))
# print(list(temp))

# a=list(filter(lambda x:x%2,range(10)))
# print(a)


# #map()

# a=list(map(lambda x:x*2,range(10)))
# print(a)

# a=list(map(lambda x,y:x+y,[1,2,3],[3,2,1,1]))
# print(a)

# # recursion()
# def recursion(n):
#     result=n
#     for i in range (1,n):
#         result*=i
#     return result

# number = int(input('input a number \t'))
# result = recursion(number)

# print('%d! is %d' % (number,result))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# number = int(input('input a number \t'))
# result = factorial(number)

# print('%d! is %d'% (number,result))


#Fibonacci

# def fab(n):
#     a1=1
#     a2=1
#     a3=1

#     if n<1:
#         print('error input')
#         return -1
    
#     while (n-2)>0:
#         a3=a1+a2
#         a1=a2
#         a2=a3
#         n-=1

#     return a3
# result = fab(20)
# if result !=-1:
#     print('Total number is %d' % result)

# def fab(n):
#     if n<1:
#         print('input error')
#         return -1
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# result = fab(20)
# if result != -1:
#     print('Total number is %d' % result)

# result = fab(35)
# if result != -1:
#     print('Total number is %d' % result)

# def hanoi(n,x,y,z):
#     if n==1:
#         print(x,'-->',z)
#     else:
#         hanoi(n-1,x,z,y)
#         print(x,'-->',z)
#         hanoi(n-1,y,x,z)
# n=int(input('input the number \t'))
# hanoi(n,'X','Y','Z')

# dict

# a=dict(one=1,two=2,three=3)
# b={'one':1,'two':2,'three':3}
# c=dict(zip(['one','two','three'],[1,2,3]))
# d=dict([('two',2),('one',1),('three',3)])
# e=(dict({'three':3,'one':1,'two':2}))
# print(a==b==c==d==e)

#set

# list1=[1,2,3,4,5,6,7,8,9,0]
# temp=list1[:]
# list1.clear()
# for i in temp:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# list1=[0,1,2,3,4,5,6,7,8,9,9,9,9,99,9,9,2,3,4,5,6]
# list1=list(set(list1))
# print(list1)

# set1={1,2,3,4,5,4,3,2,1,0}
# for i in set1:
#     print(i,end=' ')

# print(set1)

# set1.add(9)

# print(set1)
# set1.remove(0)
# print(set1)

# set1=frozenset({1,2})
# set1.add(3)

# import os
# os.getcwd()
# print(os.getcwd)

# print(os.listdir())

# os.mkdir('test')

#pickle pickling unpickling

# import pickle
# my_list=[99,549,'love']
# pickle_file= open(r'C:\Users\HITT\Documents\python\my_list.pkl','wb')
# pickle.dump(my_list,pickle_file)
# pickle_file.close()

# import pickle

# pickle_file=open(r'C:\Users\HITT\Documents\python\my_list.pkl','rb')
# my_list=pickle.load(pickle_file)
# print(my_list)



# file_name=input('input the filename you want open\t')
# f=open(file_name,'r')
# print('The content of file is\t')
# for i in f:
#     print(i)

# try-except
# try:
#     f=open('Nosuchfile.txt')
#     print(f.read())
#     f.close()

# # except OSError:
# #     print('wrong process')

# except OSError as reason:
#     print('the wrong reason is :'+ str(reason))

