def main():
    strn1 = 'pale'
    strn2 = 'paloo'
    print('Result is: {}'.format(one_away(strn1, strn2)))


'''
Complexity
Time: O(n)
Space: No additional data structures used
'''
def one_away(strn1, strn2):
    if len(strn1) == len(strn2):
        return equal_length(strn1, strn2)
    elif len(strn1) > len(strn2):
        return one_edit_away(strn2, strn1)
    else:
        return one_edit_away(strn1, strn2)


def equal_length(strn1, strn2):
    allow = 0
    for i in range(0, len(strn1)):
        if strn1[i] != strn2[i]:
            if allow == 0:
                allow = 1
            else:
                return False
    return True


# strn2 is always > strn1
def one_edit_away(strn1, strn2):
    index1 = 0
    index2 = 0
    while index1 < len(strn1) and index2 < len(strn2):
        if strn1[index1] != strn2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


if __name__ == '__main__':
    main()
