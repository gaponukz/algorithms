# https://www.eolymp.com/uk/submissions/13239161

n = int(input())
arr = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            result += 1

print(result)