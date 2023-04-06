# https://www.eolymp.com/uk/submissions/13328154

import itertools

def count_exam_scores(n, current, min_limit):
    '''
    40%
    '''
    max_limit = current - (n - 1) * min_limit + 1
    count = 0

    for score_list in itertools.product(range(min_limit, max_limit), repeat=n):
        if sum(score_list) == current:
            count += 1
    
    return count

def count_exam_scores(n, current, min_limit):
    '''
    40%
    '''
    max_limit = current - (n - 1) * min_limit + 1
    count = 0

    def generate_scores(scores, total):
        nonlocal count
        
        if len(scores) == n:
            if total == current:
                count += 1
            return
        for score in range(min_limit, max_limit):
            if total + score > current:
                break
            generate_scores(scores + [score], total + score)

    generate_scores([], 0)
    
    return count

def count_exam_scores(n, current, min_limit):
    '''
    100% (using dynamic programming)
    '''
    table = [[0] * (current + 1) for _ in range(n + 1)]
    table[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i * min_limit, current + 1):
            table[i][j] = sum(table[i-1][j-k] for k in range(min_limit, j-(i-1)*min_limit+1))

    return table[n][current]

if __name__ == '__main__':
    '''
    Висновок: повний перебір не є ефективним
    та при можливісті його потрібно замінити)
    '''
    with open("output.txt", "w", encoding="utf-8") as out_stream:
        with open("input.txt", 'r', encoding='utf-8') as input_stream:
            n = int(input_stream.readline())

            for _ in range(n):
                length, marks_sum, min_limit = list(map(int, input_stream.readline().split()))

                count = count_exam_scores(length, marks_sum, min_limit)
                out_stream.write(f"{count}\n")
