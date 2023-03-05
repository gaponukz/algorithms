k = 0
n = 10

# 1.3 a)
k += 1 # 4
i = n # 2
while i > 0: # 2 * n
    i -= 1 # 4 * (n - 1)

# T(n) = 4 + 2 + 2n + 4(n-1)

# 1.3 b)
i = n # 2
while i > 1: # 2 * log(n)
    k += 1 # 4 * log(n)
    i //= 2 # 4 * log(n)

# T(n) = 2 + log(n) (2 + 4 + 4)

# 1.3 c)
i = 0 # 2
while i < n: # 3 * (n / 2)
    j = 0 # 2 * (n / 2)
    while j < n: # 3 * (n / 2) * (n / 2)
        k += 1 # 4 * (n / 2) * (n / 2)
        j += 2 # 4 * (n / 2) * (n / 2)
    i += 2 # 4 * (n / 2)

# T(n) = 2 + (n / 2) * (3 + 2 + (n / 2) * (3 + 4 + 4) + 4)

# 1.3 d)
i  = 0 # 2
while i < n: # 3 * n
    j = 0 # 2 * n
    while j < i * i: # 4 ^ n
        k += 1 # 4 ^ n
        j += 1 # 4 ^ n
    i += 1 # 4 * (n - 1)

# T(n) = 2 + 3n + 2n + 4^n + 4^n + 4^n + 4 * (n-1)

# 1.3 e)
i = 1 # 2
while i < n: # 3 * log(n)
    j = 1 # 2 * log(n)
    while j < n: # 3 * log(n) * log(n)
        k += 1 # 4 * log(n) * log(n)
        j *= 2 # 4 * log(n) * log(n)
    i *= 2 # 4 * log(n)

# T(n) = 2 + log(n)(3 + 2 + log(n)(4 + 4) + 4)

# 1.3 f)
i = 1 # 2
while i < n: # 3 * log(n)
    j = i # 2 * log(n)
    while j < n: # 3 * log(n) * log(log(n))
        k += 1 # 4 * log(n) * log(log(n))
        j *= 2 # 4 * log(n) * log(log(n))
    i *= 2 # 4 * log(n)

# T(n) = 2 + log(n)(3 + 2 + log(log(n))(4 + 4) + 4)
