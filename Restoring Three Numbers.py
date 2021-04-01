number = list(map(int, input().split()))
maximum = max(number)
for i in range(len(number)):
    if maximum>number[i]:
        print(abs(maximum-number[i]), end=" ")