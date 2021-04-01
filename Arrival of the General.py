n = int(input())
seq = list(map(int, input().split()))
j=0
k=0
max = seq[0]
min = seq[0]
for i in range(1, n):
    if seq[i]>max:
        max = seq[i]
        j=i
    if seq[i]<=min:
        min = seq[i]
        k=i
if k>j:
    print(n-k+j-1)
else:
    print(n-k+j-2)