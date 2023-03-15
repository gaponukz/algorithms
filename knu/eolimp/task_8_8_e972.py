# https://www.eolymp.com/uk/submissions/13239446

def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

insertion_sort(data)

for date in data:
    print(*date)
