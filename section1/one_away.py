from collections import defaultdict


def is_one_away(s1, s2):
    char_counts1 = count_chars(s1)
    char_counts2 = count_chars(s2)
    keys = set(char_counts1.keys()) | set(char_counts2.keys())
    diffs = 0
    for key in keys:
        char_diff = abs(char_counts1.get(key, 0) - char_counts2.get(key, 0))
        diffs += char_diff

    return diffs <= 1


def count_chars(s):
    counts = defaultdict(lambda: 0)
    for char in s:
        counts[char] += 1
    return counts


test1 = ('pale', 'ple', True)
test2 = ('pales', 'pale', True)
test3 = ('pale', 'bale', True)
test4 = ('pale', 'bake', False)

for test in [test1, test2, test3, test4]:
    assert is_one_away(test[0], test[1]) == test[2], (test[0], test[1])