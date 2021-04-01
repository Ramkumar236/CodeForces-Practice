n, h = map(int, input().split())
width = 0
friends = list(map(int, input().split()))
for fh in friends:
    if fh > h:
        width += 2
    else:
        width += 1
print(width)
