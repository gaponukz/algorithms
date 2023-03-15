# https://www.eolymp.com/uk/submissions/13239298

def selection_sort(array):
    size = len(array)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])

n = int(input())
data = [input().strip() for _ in range(n)]

selection_sort(data)

for item in data:
    print(item)
