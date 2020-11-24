import numpy as np
import matplotlib.pyplot as plt
import random
import numpy as np
#####################################################
#reputation encoding, N= 1, 3, 5, 7, transmitted string
#####################################################
n = 1000
for _ in range(n):
    digit1 = np.random.randint(0, 2)
    print(digit1)

for _ in range(n):
    digit1 = np.random.randint(0, 2)
    digit3 = (str(digit1) * 3)
    print(digit3)

for _ in range(n):
    digit1 = np.random.randint(0, 2)
    digit5 = (str(digit1) * 5)
    print(digit5)

for _ in range(n):
    digit1 = np.random.randint(0, 2)
    digit7 = (str(digit1) * 7)
    print(digit7)

#####################################################
# transmite the code with p < 0.5
#####################################################
'''def bernoulli(p):
    if rand <= p:
        return 1
    else:
        return 0'''

binary_input = open('generatedcode.txt', 'w')
s_prime = open('transmittedcode.txt', 'w')
result_file = open('myresult.txt', 'w')
##################################################



