# https://www.eolymp.com/uk/submissions/13307000

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0 , 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            
            else:
                array[k] = righthalf[j]
                j += 1
            
            k += 1
        
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

if __name__ == '__main__':
    n = int(input())
    arr = []

    for i in range(n):
        a, b = map(int, input().split())
        arr.append(((a, i), b))
    
    merge_sort(arr)

    for i in range(n):
        print(arr[i][0][0], arr[i][1])

