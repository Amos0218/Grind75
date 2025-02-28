from collections import Counter

# 字串範例
s = "aabbcc"
counter_s = Counter(s)
print(counter_s)  # Output: Counter({'a': 2, 'b': 2, 'c': 2})

# 列表範例
lst = [1, 2, 2, 3, 3, 3]
counter_lst = Counter(lst)
print(counter_lst)  # Output: Counter({3: 3, 2: 2, 1: 1})