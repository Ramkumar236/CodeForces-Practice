year = int(input())
isTrue = True
while isTrue:
    year += 1
    a = year//1000
    b = year//100%10
    c = year//10%10
    d = year%10
    if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
        isTrue = False

print(year)