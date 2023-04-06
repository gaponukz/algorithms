# https://www.eolymp.com/uk/submissions/13439241
mp = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '['
}

s = input().strip()
st = []
success = True

for ch in s:
    if ch not in '()[]{}':
        continue

    elif ch in '([{':
        st.append(ch)

    elif st and mp[ch] == st[-1]:
        st.pop()
    
    else:
        success = False
        break

if success and st:
    success = False

print('yes' if success else 'no')

