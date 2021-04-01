word = input()
count1 =0
count2 =0
for i in range(len(word)):
    if word[i] >='a' and word[i] <= 'z':
        count1 += 1
    elif word[i] >= 'A' and word[i] <= 'Z':
        count2 += 1

if count1 >= count2:
    print(word.lower())
else:
    print(word.upper())