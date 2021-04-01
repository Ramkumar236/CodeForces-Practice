a, b = map(int, input().split())
isTrue = True
year = 0
while isTrue:
    if a < b or a == b:
        year += 1
        a = a * 3
        b = b * 2
    else:
        isTrue = False
print(year)
