from collections import Counter
s = "aabbcdd"
c = Counter(s)
for ch in s:
    if c[ch] == 1:
        print(ch)
        break