import matplotlib.pyplot as plt
import random
import numpy as np
import csv
from numpy import random
#######################################################
m = 0
while m<= 1000:
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
    #function for comparing first two culmn, in dorst compare nemikone, byad har mosavi budan 1 bede
    # only for n=1 chon majority nadarim faghat 1 bit e
    def accuracy(n):
        if (generate(n) ==transmittedcode(n)):
            acc = 1
        else:
            acc = 0
        return acc
#####################################################
    #function to evaluate majarity for n = 3, 5, 7
    # in mikhad tranmittedcode ro barresi kone, age tedade 1 bishtar bud,
    # bezare 1 vali man radif balad nistm joda konam


#######################################################
#writing in txt and calling the above functions
    # opening the csv file in 'w' mode
    file = open('generatedcode.csv', 'w', newline='')
    with file:
        # identifying header
        header = ['generated code', 'transmitted code', 'evaluate']
        writer = csv.DictWriter(file, fieldnames=header)

        # writing data row-wise into the csv file
        writer.writeheader()
        for i in range (m):
            writer.writerow({'generated code': generate(1),
                         'transmitted code': transmittedcode(1),
                         'evaluate': accuracy(1)})

        for i in range (m):
            writer.writerow({'generated code': generate(3),
                         'transmitted code': transmittedcode(3),
                         'evaluate': accuracy(3)})


        for i in range (m):
            writer.writerow({'generated code': generate(5),
                         'transmitted code': transmittedcode(5),
                         'evaluate': '       --'})

        for i in range (m):
            writer.writerow({'generated code': generate(7),
                         'transmitted code': transmittedcode(7),
                         'evaluate': '       --'})












