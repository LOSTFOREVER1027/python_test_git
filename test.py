#just for fun
list1=[9,8,7,6,5,4,3,2,1,0]
list1.reverse()
print(list1)

list2=list1[0:5]
print(list2)

for i in list2:
    print(i)
    print('i')
    print("i")



# format
print("{0} love {1} . {2}".format('I','my','com'))
print('{a} love {b} . {c}'.format(a='I',b='me',c='!'))
print('%c'%97)

print('%c%c%c%c%c' % (70,105,115,104,67))

print('%d 10 is %o 8' % (1027,1027))

print('%d in kexue is %e' % (1027,1027))

str1='一支穿云箭，千军万马来相见；'
str2='两幅忠义胆，刀山火海提命现。'

print('%s%s' % (str1,str2))

print('a\'')
print('a\"')
print('\"a\"')
print('1\n')
print('2\t3')
print('3\v4')

print('5\r')
print('6\f')


#
a=list()
print(a)

b=list('love')
print(b)

c=list((0,1,2,3,4,5))
print(c)

print(max(list1))

print(min(list1))

print(sum(list1))

print(list1,list1.sort(),list1)

print(list1)

list2=list1.sort()

print(list2)

list1=[9,8,7,6,5,4,3,2,1,0]
list2=list1[:]
print(list1)
print(list2)

list1.sort()

print(list1)

sorted(list2)

print(list2)
print(sorted(list2))

def myfunction():
    print('it is my first function')
    print('i \'d like to say sth.')
    print('thanks to cctv tvb\n')

print(myfunction())

def function_sin(x):
    print((x))

print(function_sin(2))

def add(num1,num2):
    return num1+num2
print(add(1,2))