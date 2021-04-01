name = list(map(str,input()))
count = 0
temp = []
for letter in name:
    if letter not in temp:
        count += 1
        temp.append(letter)

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")