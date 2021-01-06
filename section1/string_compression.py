def compress(s):
    if len(s) <= 2:
        return s

    compressed = list()
    current = s[0]
    count = 1
    idx = 1

    while idx < len(s):
        if s[idx] != current:
            compressed.extend([current, count])
            current = s[idx]
            count = 1
        else:
            count += 1

        idx += 1

    compressed.extend([current, count])

    if len(compressed) >= len(s):
        return s
    else:
        return ''.join(str(c) for c in compressed)


test1 = ('ab', 'ab')
test2 = ('abb', 'abb')
test3 = ('aabb', 'aabb')
test4 = ('aaabb', 'a3b2')
test5 = ('aabcccccaaa', 'a2b1c5a3')

for test in [test1, test2, test3, test4, test5]:
    assert compress(test[0]) == test[1]