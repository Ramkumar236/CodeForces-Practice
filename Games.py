num= int(input())
h = []
a = []

for _ in range(num):
    l,n = map(int, input().split())
    h.append(l)
    a.append(n)
    count = 0

for i in range(num):
    for j in range(num):
        if i!=j and h[i]==a[j]:
            count += 1
print(count)