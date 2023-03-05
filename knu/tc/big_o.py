import itertools

count = 0
for digits in itertools.product(range(1, 10), range(10), range(10), range(10), range(10), range(10)):
    if len(set(digits)) == 6:
        count += 1
        
print(count)
