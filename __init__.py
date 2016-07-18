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
'''


stringus = "This {} text locate {} in {} right place".format('<10', '>10', '^10')
print (stringus)