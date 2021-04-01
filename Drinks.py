n = int(input())
vol = list(map(int, input().split()))
sum=0
for i in range(n):
    sum = sum+vol[i]
print("{0:.12f}".format(sum/n))