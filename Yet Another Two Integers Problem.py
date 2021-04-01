t = int(input())
while t:
    a, b = map(int, input().split())
    s = abs(a-b)
    if s%10 == 0:
        print(s//10)
    else:
        print(s//10+1)