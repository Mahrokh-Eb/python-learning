#tamrini
import matplotlib.pyplot as plt
import random
import numpy as np
import csv
from numpy import random
#######################################################
m = 0
while m<= 10:
    # funtion to generate the code, (coding)
    def generate(n):
        for i in range(n):
            digit = np.random.randint(0, 2)
            digit = (str(digit) * n)
            # convert digit to list
            digit_map = map(int, digit)
            digit_list = list(digit_map)
            return digit_list
    m+=1
#######################################################
    #transmition code-n=1
    # function to evaluate probability and transmitting (send the code)
    def transmittedcode(n):
        k = 1
        list = []
        while (k < n + 1):
            probability = random.uniform(0, 0.5)
            if (probability >= 0.25):
                probg = 1
                list.append(1)
            else:
                probg = 0
                list.append(0)
            k += 1
        return list
#######################################################
    #function for comparing first two culmn

    def accuracy(n): # 1
        print(generate(n))
        if (generate(n) == transmittedcode(n)):
            print('yes')
        else:
            print('no')

    accuracy(1)

a=generate(1)
a=[1,1,0,1]
1
1
0
1
