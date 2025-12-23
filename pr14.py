from collections import Counter
lst = [1, 2, 3, 2, 4, 1]
duplicates = [k for k, v in Counter(lst).items() if v > 1]
print(duplicates)