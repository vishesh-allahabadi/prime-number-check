# Switching numbers

from re import A


a = input('a:')
b = input('b:')
print('a = ' + a)
print('b = ' + b)


c = a
a = b
b = c

print('a = ' + a)
print('b = ' + b)
