# Simulation of Die Throwing (using a list)

#Simulation of Die Throwing (using a list)
import random
import matplotlib.pyplot as plt
test_data = [10, 50, 100, 500]  # this will keep track of the results
n = 1000  # this can be easily changed for different sample sizes

for i in range(n):
    result = random.randint(1, 4)
    test_data[result - 1] = test_data[result - 1] + 1

for i in range(0, 4):
    print("Number of ", i + 1, "'s: ", test_data[i])

test_data(1000).plot()
plt.plot(test_data(1000))
plt.show()

# To change the number of sides on the die, change the size of
# test_data and the range for the random number.