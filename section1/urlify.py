def URLify(s, true_length):
    as_list = list(s)
    num_spaces = count_spaces(as_list, true_length)
    idx = true_length - 1
    while idx >= 0:
        current = as_list[idx]
        if current == ' ':
            insert_space(as_list, idx, num_spaces)
            idx -= 1
            num_spaces -= 1
        if idx > 0:
            new_pos = idx + (num_spaces * 3) - 1
            as_list[new_pos] = as_list[idx]
        idx -= 1
    back_to_string = ''.join(as_list)
    return back_to_string


def count_spaces(s, true_length):
    num_spaces = len([c for c in s[:true_length] if c == ' '])
    return num_spaces


def insert_space(s, idx, num_spaces):
    s[idx + num_spaces * 3 - 1] = '0'
    s[idx + num_spaces * 3 - 2] = '2'
    s[idx + num_spaces * 3 - 3] = '%'


test1 = 'nospace'
assert URLify(test1, true_length=7), URLify(test1, true_length=7)

test2 = 'a space  '
assert URLify(test2, true_length=7) == 'a%20space', URLify(test2, true_length=7)

test3 = ' spaceatstart  '
assert URLify(test3, true_length=13) == '%20spaceatstart', URLify(test3, true_length=13)

test4 = 'double  space     '
assert URLify(test4, true_length=13) == 'double%20%20space', URLify(test4, true_length=13)

