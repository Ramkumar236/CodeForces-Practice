n, t = map(int, input().split())

str = list(map(str,input()))
for i in range(t):
    j = 0
    while j < (n-1):
        if str[j] == "B" and str[j+1] == "G":
            str[j] = "G"
            str[j+1] = "B"
            j += 2
        else:
            j += 1

print("".join(str))
