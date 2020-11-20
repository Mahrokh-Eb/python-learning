import random

test_data = [1, 2, 3, 4]
n1 = 10
n2 = 50
n3 = 100
n4 = 500
n5 = 10000

for i in range(n1):
    result = random.randint(1, 4)
    test_data[result - 1] = test_data[result - 1] + 1
    print("Number of ", i + 1, "'s: ", test_data[i])
    # check odd number
    count = 0
'''    def check_odd(numbers):
        count = 0
        for i in test_data:
            if i % 2 == 0:
                pass
            else:
                count += 1
        return count
'''