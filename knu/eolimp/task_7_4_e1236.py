# https://www.eolymp.com/uk/submissions/13229150

import typing
from collections import defaultdict

T = typing.TypeVar("T", int)

def binary_search(data: list[T], x: T) -> T:
    low, high = 0, len(data) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] > x:
            result = data[mid]
            high = mid - 1

        else:
            low = mid + 1

    return result

def get_letters_info(string: str) -> defaultdict[str, list[int]]:
    result = defaultdict(list)

    for index, char in enumerate(string):
        result[char].append(index)

    return result

def main():
    n = int(input())
    obscene_words = [input() for _ in range(n)]
    text = input()

    text_letters_info = get_letters_info(text)
    result = None

    for word in obscene_words:
        word_letters_info = get_letters_info(word)
        
        if all(len(word_letters_info[char]) <= len(text_letters_info[char]) for char in word_letters_info):
            text_letters_info_copy = text_letters_info
            indexes: list[int] = []

            for char in word:
                last = indexes[-1] if indexes else -1
                item = binary_search(text_letters_info_copy[char], last)

                if item != -1:
                    indexes.append(item)
                
                else:
                    break
            
            else:
                num = indexes[-1] + 1
                result = result if result and result < num else num

    if result:
        print(f"YES {result}")

    else:
        print("NO")

if __name__ == "__main__":
    main()
