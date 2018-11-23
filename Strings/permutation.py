def main():
    str1 = 'taco cat'
    str2 = 'atoc tac'
    print('Result is: {}'.format(is_permutation(str1, str2)))


'''
Complexity
Time: O(n log(n)). Assuming mergesort is used
'''
def is_permutation(str1, str2):
    # Base cases
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2


if __name__ == '__main__':
    main()
