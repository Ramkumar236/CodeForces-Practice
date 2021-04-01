num = int(input())
y = 0
while num:
    x = num%10
    if x == 4 or x == 7:
        y += 1
    num = num//10
if y == 4 or y == 7 or y == 47 or y == 74:
    print("YES")
else:
    print("NO")