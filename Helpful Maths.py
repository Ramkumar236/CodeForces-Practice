n = list(map(str, input().split("+")))
n = sorted(n)
if len(n)<2:
    print("".join(n))
else:
    n = "+".join(n)
    print(n)