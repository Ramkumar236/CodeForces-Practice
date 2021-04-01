n = int(input())
count = 0
for i in range(n):
    p, q = map(int,input().split())
    remaining_capacity = q-p
    if remaining_capacity >= 2:
        count += 1

print(count)