num = int(input())
X=0
for _ in range(num):
    bits = input()
    if bits == "X++" or bits == "++X":
        X += 1
    elif bits == "X--" or bits == "--X":
        X -= 1
print(X)