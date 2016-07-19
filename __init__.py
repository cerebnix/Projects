'''
l= list(range (1,31))

l = input("Enter text")
print (l * 2)

for line in open ('test.txt'):
    print (line)

f = open ("test.txt")
for line in f.readlines():
    print(line)

import sys
print(sys.copyright, '\n\n', '\n sys.platform', sys.platform, '\n sys.path', sys.path, '\n sys.modules', sys.modules)


stringus = "This {first:>10s} text locate {first} in {third: <20s} right place".format(first='10', second='20', third='30')
print (stringus)

l=[1, 22, 333, 4444, 5555]
t=(10, 20, 30, 40, 50)

print(t.__getitem__(3))
#l1=str(l.__getitem__(2))
#print(l1)
print("{:>10}".format(str(l.__getitem__(2))))

print(l[0:4])

print (tuple(range(100, 20, -5)))

s1 = "Never give UP!!!"
print (s1.__len__())

for i in s1:
    print (i)
'''

s1 = "Never give UP!!!"

b = '!!!!' in s1

print(s1.replace("!!!", "QQQQQ"))