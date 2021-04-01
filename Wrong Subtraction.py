num,n = map(int,input().split())
for _ in range(n):
    if num%10 == 0:
        num = num//10
    else:
        num = num-1
print(num)