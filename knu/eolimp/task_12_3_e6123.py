# https://www.eolymp.com/uk/submissions/13382994

with open("output.txt", "w", encoding="utf-8") as out_stream:
    with open("input.txt", 'r', encoding='utf-8') as input_stream:
        while True:
            input_data = input_stream.readline().strip().split()
            s: str
            n: int
            st: list[int] = []

            if len(input_data) > 1:
                s, n = input_data
                n = int(n)
            
            else:
                s, n = input_data[0], 0

            if s == "exit":
                out_stream.write("bye\n")
                break

            if s == "push":
                st.append(n)
                out_stream.write("ok\n")

            elif s == "size":
                out_stream.write(f"{len(st)}\n")
            
            elif s == "pop":
                if len(st) == 0:
                    out_stream.write("error\n")
                
                else:
                    out_stream.write(f"{st[-1]}\n")
                    st.pop()
                
            elif s == "back":
                if len(st) == 0:
                    out_stream.write("error\n")
                
                else:
                    out_stream.write(f"{st[-1]}\n")
                
            elif s == "clear":
                st.clear()
                out_stream.write("ok\n")

