num = int(input())
for _ in range(num):
    a,b = map(int, input().split())
    ans = 0
    if a%b == 0:
        print(ans)
    else:
        k = a//b
        ans = abs(b * (k+1) - a)
        print(ans)