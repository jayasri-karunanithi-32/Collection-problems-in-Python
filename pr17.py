nums = [1, 2, 4, 5]
n = 5
missing = set(range(1, n+1)) - set(nums)
missing_value=missing.pop()
print(missing_value)
