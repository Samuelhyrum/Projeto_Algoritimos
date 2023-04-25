def counting_sort(s):
    count = [0] * 26
    for c in s:
        count[ord(c.lower()) - ord('a')] += 1
    res = ""
    for i in range(26):
        res += chr(ord('a') + i) * count[i]
    return res


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return (first_string, second_string, False)
    word_1 = counting_sort(first_string)
    word_2 = counting_sort(second_string)
    return (word_1, word_2, word_1 == word_2)
