n = int(input())
max = 0
total = 0
for _ in range(n):
    a,b = map(int,input().split())
    total = total+b
    total = total-a
    if total>max:
        max = total
print(max)