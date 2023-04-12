# https://www.eolymp.com/uk/submissions/13490280
from collections import deque

with open("output.txt", "w", encoding="utf-8") as out_stream:
    with open("input.txt", 'r', encoding='utf-8') as input_stream:
        multideque: dict[int, deque] = {}
        n = int(input_stream.readline().strip())

        for _ in range(n):
            command, slot, *args = input_stream.readline().strip().split()
            number = args[0] if args else None

            if (command == "popfront" or command == "popback") and not slot in multideque:
                out_stream.write(f"error\n")
            
            elif command == "pushback":
                if slot in multideque:
                    multideque[slot].append(number)
                
                else:
                    multideque[slot] = deque([number])
            
            elif command == "pushfront":
                if slot in multideque:
                    multideque[slot].appendleft(number)
                    
                else:
                    multideque[slot] = deque([number])
                
            elif command == "popfront":
                if len(multideque[slot]) > 0:
                    out_stream.write(f"{multideque[slot].popleft()}\n")
                    
                    if len(multideque[slot]) == 0:
                        del multideque[slot]
                
                else:
                    out_stream.write(f"error\n")
                
            elif command == "popback":
                if len(multideque[slot]) > 0:
                    out_stream.write(f"{multideque[slot].pop()}\n")

                    if len(multideque[slot]) == 0:
                        del multideque[slot]
                
                else:
                    out_stream.write(f"error\n")
