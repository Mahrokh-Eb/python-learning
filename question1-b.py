'''
Programmer: Mahrokh Ebrahimi
Discription: Suppose X is a random variable denoting the outcome of a die toss.
Based on the mathematical analysis, what is the probability that X has odd value
Date: 20/20/2020
'''
countOdd = 0
import random
test_data = [1, 2, 3, 4]
result = random.randint(1, 4)
if result % 2 == 0:
    print('x is even')
if result % 2 != 0:
    countOdd +=1
    print('x is odd with probability: ', countOdd/2)

