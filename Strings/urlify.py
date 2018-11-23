def main():
    str = 'hello world'
    print('Original: {}'.format(str))
    print('Result is: {}'.format(urlify(str)))


'''
Complexity
Time: O(n), since each element is looked at once
'''
def urlify(str1):
    result = []

    for c in str1:
        if c == ' ':
            result.append('%20')
        else:
            result.append(c)

    return ''.join(str(x) for x in result)


if __name__ == '__main__':
    main()
