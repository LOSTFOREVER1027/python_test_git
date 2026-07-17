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

