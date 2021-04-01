t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    isTrue = True
    lst = sorted(lst)
    for j in range(1,n):
        if lst[j]-lst[j-1]>1:
            print("NO")
            isTrue = False
            break
    if isTrue:
        print("YES")