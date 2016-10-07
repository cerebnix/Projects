#!/usr/bin/env python3

'''
Just file for tests


start = 10
stop = 0

while stop < start:
    start = int(input("Please enter start point for range: "))
    stop = int(input("Please enter stop point for range: "))

for a in range(start, stop):
    if a == 13 or a == 15 or a == 17:
        continue+++
    if a == 19:
        break
    print(a)




import keyword

print(keyword.kwlist)

for i in keyword.kwlist:
    print(i)

a = keyword.kwlist
print(type(a))

a = ('hello world')
b = tuple('hello world')

print (a,b)


def myf(c, b, a=3):
    print(a +c + b)
    return a, b, c


print(type(myf(0, 10, 10)))


def myf2(*args):
    return args

def myf3(**kwargs):
    return kwargs

#a = (myf2(input("Enter all what you want ")))

#for z in a:
#    print(z, type(z))
try:
    vv = input("Enter all what you want ")
    aa = (myf3(vv))
except TypeError:
    print("Wrong type {}".format(vv))

for zz in aa:
    print(zz, type(zz))

=============================
try:
    vv = dict(input("Enter all what you want "))

    def myf2(*args):
      return args

    def myf3(**kwargs):
     return kwargs

    print("vv={}".format(vv))
    print("args={}".format(myf2(vv)))
    print("kwargs={}".format(myf3(vv)))

except TypeError:
    print("Wrong type")

except ValueError:
    print("Wront value")


'''