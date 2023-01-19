import random

def __hash(size: int):
    # get family of functions
    seed = int(random.random() * size) + 32

    def _hash(data: str):
        result = 1

        for char in data:
            result = (seed * result + ord(char)) & 0xFFFFFFFF
        
        return result

    return _hash

def find_min(data, function):
    return min([function(item) for item in data])

def signature(data, functions):
    # get mins of hash values
    return [find_min(data, function) for function in functions]

def similarity(data1: list, data2: list, e=0.1) -> float:
    # O(2(nk) + k) ~ O(nk) where k - function count, n - data lenght
    functions_count = int(1 / pow(e, 2))
    functions = [__hash(functions_count) for _ in range(functions_count)]

    sig_a = signature(data1, functions)
    sig_b = signature(data2, functions)

    equal_count  = 0

    for i in range(functions_count):
        # how much min values are matched
        if (sig_a[i] == sig_b[i]):
            equal_count += 1
    
    return equal_count / functions_count # ~ Jacquard coefficient

def jacquard_coefficient(set1: set, set2: set):
    return len(set1 & set2 ) / len(set1 | set2)

if __name__ == "__main__":
    data1 = ['apple', 'orange', 'data', 'cool', 'wow']
    data2 = ['apple', 'post', 'data', "cock", 'wow']

    print(jacquard_coefficient(set(data1), set(data2)))
    print(similarity(data1, data2, e=0.005))
