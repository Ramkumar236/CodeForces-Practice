num = int(input())
count = 0
for _ in range(num):
    x1,x2,x3 = input().split()
    known_ans = int(x1)+int(x2)+int(x3)
    if known_ans > 2 or known_ans == 2:
        count = count+1
print(count)