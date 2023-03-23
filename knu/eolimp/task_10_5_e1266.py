# https://www.eolymp.com/uk/submissions/13318127

def magic(position: int, _sum: int, vector: list[int]):
    global ans # some shitcode, but...
    if ans == n or _sum > n:
        return

    if position == len(vector):
        if _sum > ans and _sum <= n:
            ans = _sum

        return

    magic(position + 1, _sum + vector[position], vector)
    magic(position + 1, _sum, vector)

with open("output.txt", "w", encoding="utf-8") as out_stream:
    with open("input.txt", 'r', encoding='utf-8') as input_stream:
        while (data := input_stream.readline().strip()):
            n, _, *vector = data.split()

            ans = 0
            n = int(n)

            magic(0, 0, [int(item) for item in vector])
            out_stream.write(f"sum:{ans}\n")
