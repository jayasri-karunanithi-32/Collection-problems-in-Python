from collections import defaultdict
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
group = defaultdict(list)
for word in words:
    group["".join(sorted(word))].append(word)
print(list(group.values()))
