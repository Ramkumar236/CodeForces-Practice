import re
sentence = input()
sentence = re.findall(r'\{(.*?)\}', sentence)
sentence = set(map(str, sentence[0].split(", ")))
if sentence == {""}:
    print(0)
else:
    print(len(sentence))