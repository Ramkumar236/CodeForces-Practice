word_t = list(map(str, input()))
word_s = list(map(str, input()))
rev_word_s = list(reversed(word_s))

if len(word_s) != len(word_t):
    print("NO")
elif word_t == rev_word_s:
    print("YES")
else:
    print("NO")