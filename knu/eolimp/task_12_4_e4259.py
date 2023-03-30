# https://www.eolymp.com/uk/submissions/13383006

class StackMin:
    def __init__(self):
        self.st = []

    def minimum(self) -> int:
        return self.st[-1][1]

    def push(self, new_element: int) -> None:
        minima = new_element if not self.st else min(new_element, self.st[-1][1])
        self.st.append((new_element, minima))

    def pop(self) -> None:
        self.st.pop()

with open("output.txt", "w", encoding="utf-8") as out_stream:
    with open("input.txt", 'r', encoding='utf-8') as input_stream:
        n = int(input_stream.readline().strip())
        st = StackMin()

        for i in range(n):
            a, *args = map(int, input_stream.readline().strip().split())
            if a == 1:
                b = args[0]
                st.push(b)

            elif a == 2:
                st.pop()

            elif a == 3:
                print(st.minimum())

