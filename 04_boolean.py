#!/usr/bin/env python3

a = True
b = False
x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if a or b:
    print('expression is true')
else:
    print('expression is false')

#as b is false, then expression is true
if not b:
    print('expression is true')
else:
    print('expression is false')

#as a is true, then expression is false
if not a:
    print('expression is true')
else:
    print('expression is false')

#is y in x
if y in x:
    print('expression is true')
else:
    print('expression is false')

#is leaf in x
if 'leaf' in x:
    print('expression is true')
else:
    print('expression is false')

#is tree in x
if 'tree' in x:
    print('expression is true')
else:
    print('expression is false')

#is y is x subzero - ie are they the same object
if y is x[0]:
    print('expression is true')
else:
    print('expression is false')

print(str(id(y)) + ' id of y')
print(str(id(x[0])) + ' id of x subzero')
if id(y) == id(x[0]):
    print('They are same object')
else:
    print('They are not same object')

#is y not x subzero - ie are they the same object
if y is not x[0]:
    print('expression is true')
else:
    print('expression is false')

#is y not x subone - ie are they the same object
if y is not x[1]:
    print('expression is true')
else:
    print('expression is false')