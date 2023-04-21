for a in range(770):
    if all(a % i == 0 for i in [2, 5, 7, 11]):
        print(a)