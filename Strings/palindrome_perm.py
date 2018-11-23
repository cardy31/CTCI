def main():
    strin = 'tttaacoocazt'
    print('Result is: {}'.format(is_permutation(strin)))


'''
Complexity
Time: O(n). Sort is n log(n), but we have to check each element of the string, so n + n log(n) becomes O(n)
'''
def is_permutation(strin):
    # Base cases
    strin = sorted(strin)
    print(strin)

    # Even
    if len(strin) % 2 == 0:
        for i in range(0, len(strin), 2):
            if strin[i] != strin[i + 1]:
                return False
        return True

    # Odd
    allowance = 0
    i = 0
    while i < len(strin):
        # if i is at the last index of the string
        if i == len(strin) - 1:
            if allowance == 0:
                return True
            return False
        if strin[i] != strin[i + 1]:
            if allowance == 0:
                allowance += 1
                i += 1
            else:
                return False
        i += 2
    return True


if __name__ == '__main__':
    main()
