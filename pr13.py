from collections import Counter
s = "interview"
vowels = "aeiou"
vowel_count = {v: s.count(v) for v in vowels if v in s}
print(vowel_count)