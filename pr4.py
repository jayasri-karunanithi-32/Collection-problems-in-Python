from collections import Counter
a= [1, 1, 2, 3, 3, 3]
ans=Counter(a).most_common(1)[0][0]
print(ans)