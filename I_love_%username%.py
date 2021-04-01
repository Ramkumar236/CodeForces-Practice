n = int(input())
lst = list(map(int, input().split()))
max = lst[0]
min = lst[0]
count = 0
for i in range(0,n):
    if lst[i]>max:
        max = lst[i]
        count += 1
    if lst[i]<min:
        min = lst[i]
        count += 1
print(count)