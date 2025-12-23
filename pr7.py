d = {"a": 3, "b": 1, "c": 2}
ans = dict(sorted(d.items(), key=lambda x: x[1]))
print(ans)