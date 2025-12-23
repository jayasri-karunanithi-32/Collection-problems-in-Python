d = {"a": 10, "b": 25, "c": 15}
ans=max(d, key=d.get)
print(ans)