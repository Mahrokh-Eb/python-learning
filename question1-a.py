'''
Programmer: Mahrokh Ebrahimi
Discription: simulate the tossing of a 4-sided fair die, for t =10, 50, 100, 500 and 1000 tosses.
Based on the simulation,what is the estimated probability of obtaining an odd number?
Date: 20/20/2020
'''

import random

test_data = [1, 2, 3, 4]
n1 = 10
n2 = 50
n3 = 100
n4 = 500
n5 = 10000

count = 0
for i in range(n1):
    result = random.randint(1, 4)
    print(result)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 10, countof odd numbers= ',count)
print('probabilityn1= ', count/n1)


for i in range(n2):
    result = random.randint(1, 4)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 50, count of odd numbers= ',count)
print('probabilityn1= ', count/n2)


for i in range(n3):
    result = random.randint(1, 4)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 100, count of odd numbers= ',count)
print('probabilityn1= ', count/n3)


for i in range(n4):
    result = random.randint(1, 4)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 500, count of odd numbers= ',count)
print('probabilityn1= ', count/n4)


for i in range(n5):
    result = random.randint(1, 4)
    if i % 2 == 0:
        pass
    else:
        count += 1
print('when n is 1000, count of odd numbers= ',count)
print('probabilityn1= ', count/n5)