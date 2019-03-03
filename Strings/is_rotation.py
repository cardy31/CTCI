def main():
    str1 = 'erbottlewat'
    str2 = 'waterbottle'
    print('Result is: {}'.format(is_rotation(str1, str2)))


'''
Complexity
Time: O(n). Assuming the check for substring is O(n)
'''
def is_rotation(s1, s2):
    # Base cases
    length = len(s1)

    if length == len(s2) and length > 0:
        s1s1 = s1 + s1
        return s2 in s1s1
    return False


if __name__ == '__main__':
    main()
