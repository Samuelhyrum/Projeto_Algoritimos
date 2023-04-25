def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    elif word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word[1:-1], 0, - 1)
