n = int(input())
panagram = list(map(str, input().lower()))
panagram = set(panagram)
if len(panagram) == 26:
    print("YES")
else:
    print("NO")
