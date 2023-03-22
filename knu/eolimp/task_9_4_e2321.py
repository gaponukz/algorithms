# https://www.eolymp.com/uk/submissions/13306848

def qsort(array, a, b):
     if a >= b:
        return

     pivot = array[a + (b - a) // 2]
     left = a
     right = b

     while True:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

     qsort(array, a, right)
     qsort(array, right + 1, b)

n = int(input())
arr = [int(i) for i in input().split()]

qsort(arr, 0, len(arr) - 1)
print(*arr)
