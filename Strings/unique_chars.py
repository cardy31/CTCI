def main():
    string = 'robert'
    print('Result is: {}'.format(unique_chars_with_structure(string)))
    print('Result is: {}'.format(unique_char_without_structure(string)))


'''
Complexity
Time: O(n). An argument could be made for it being O(1) since it will never go for more than 128 times.
Space: O(1) It requires a constant amount of space.
'''
def unique_chars_with_structure(string):
    # Base cases
    if len(string) > 128:
        return False
    if len(string) == 0:
        return True

    store = [0] * 128
    for c in string:
        if store[ord(c)] != 0:
            return False
        store[ord(c)] += 1
    return True


'''
Complexity
Time: O(n^2)
Space: O(1)
'''
def unique_char_without_structure(string):
    # Base cases
    if len(string) > 128:
        return False
    if len(string) == 0:
        return True

    for i in range(0, len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


if __name__ == '__main__':
    main()