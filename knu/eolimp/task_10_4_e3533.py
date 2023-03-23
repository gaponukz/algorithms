# https://www.eolymp.com/uk/submissions/13318193

def combinations(array: list) -> list[list]:
    if len(array) == 0:
        return [[]]
    
    result = []
    
    for item in combinations(array[1:]):
        result += [item, item+[array[0]]]
    
    return result

def find_min(input_data: list[tuple], value: int) -> int:
    min_element = float('inf')

    for item in combinations(input_data):
        if item:
            point, time = list(map(sum, zip(*item)))

            if point >= value:
                if min_element > time:
                    min_element = time

    return min_element if min_element != float('inf') else -1

if __name__ == '__main__':
    n, value = list(map(int, input().split()))
    input_data = [tuple(map(int, input().split())) for _ in range(n)]

    print(find_min(input_data, value))
