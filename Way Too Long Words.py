num = int(input())

for i in range(num):
    words = input()
    if len(words) > 10:
        print(f"{words[0]}{len(words)-2}{words[-1]}")
    else:
        print(words)