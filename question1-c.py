'''
Programmer: Mahrokh Ebrahimi
Discription: Repeat parts (a), if even sides are twice as likely as odd sides,
and both even sides are equiprobable and both odd sides are equiprobable.
a- simulate the tossing of a 4-sided fair die, for t =10, 50, 100, 500 and 1000 tosses.
Based on the simulation,what is the estimated probability of obtaining an odd number?
Date: 12/30/2020
'''

import random
import numpy

test_data = [1, 2, 3, 4]
n1 = 10
n2 = 50
n3 = 100
n4 = 500
n5 = 10000

count = 0
for i in range(n1):
    result= numpy.random.choice(numpy.arange(1,4), p=[0.1, 0.8, 0.1])
    print(result)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 10, count of odd numbers= ',count)
print('probabilityn1 = ', count/n1)


for i in range(n2):
    result= numpy.random.choice(numpy.arange(1,4), p=[0.1, 0.8, 0.1])
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 50, count of odd numbers= ',count)
print('probabilityn1= ', count/n2)


for i in range(n3):
    result= numpy.random.choice(numpy.arange(1,4), p=[0.1, 0.8, 0.1])
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 100, count of odd numbers= ',count)
print('probabilityn1= ', count/n3)


for i in range(n4):
    result= numpy.random.choice(numpy.arange(1,4), p=[0.1, 0.8, 0.1])
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 500, count of odd numbers= ',count)
print('probabilityn1= ', count/n4)


for i in range(n5):
    result= numpy.random.choice(numpy.arange(1,4), p=[0.1, 0.8, 0.1])
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 1000, count of odd numbers= ',count)
print('probabilityn1= ', count/n5)
