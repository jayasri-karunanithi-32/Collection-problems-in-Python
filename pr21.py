lst = [1, 2, 3, 4, 5, 6]
even = sum(1 for x in lst if x % 2 == 0)
odd = sum(1 for x in lst if x % 2 != 0)
print("Even:", even, "Odd:", odd)
