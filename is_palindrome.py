def is_palindrome(word):
    ''' checks if word is a palindrome '''
    n = len(word)
    left = 0
    right = n - 1

    while left < right:
        # print(left, right, word[left], word[right])
        if word[left] != word[right]:  # mismatch, no palindrome
            return False
        left += 1
        right -= 1

    return True  # matches all the way, a palindrome


def is_palindrome2(word):
    ''' checks if word is a palindrome '''
    n = len(word)

    for i in range(n):
        # print(i, word[i], word[n-i-1])
        if word[i] != word[n - 1 - i]:  # mismatch, no palindrome
            return False

    return True  # matches all the way, a palindrome


def is_palindrome3(word):
    ''' checks if word is a palindrome '''
    return word == word[::-1]  # does word equal its reverse
