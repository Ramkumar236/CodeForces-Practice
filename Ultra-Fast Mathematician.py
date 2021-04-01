n = list(map(int, input()))
m = list(map(int, input()))

for i in range(0, len(m)):
    print(n[i]^m[i], end="")