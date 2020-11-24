'''
Programmer: Mahrokh Ebrahimi
Discription: Suppose X is a random variable denoting the outcome of a die toss.
Based on the mathematical analysis, what is the probability that X has odd value
Date: 20/20/2020
'''
import random
countOdd = 0
test_data = [1, 2, 3, 4]

while True:
    result = random.randint(1, 4)
    try:
        if result /2 != 0:
            countOdd =+ 1
            print('probability of obtaining odd number is= ', countOdd/4)
        break
    except:
        print('result is even')


