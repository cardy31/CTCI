def main():
    mystr = '????'
    # Prints "1010"
    print(replacer(mystr))


def replacer(s):
    tracker = 1
    new_str = ''

    for i in range(0, len(s)):
        if s[i] == '?':
            if tracker == 1:
                new_str += str(1)
                tracker = 0
            else:
                new_str += str(0)
                tracker = 1
        else:
            new_str += s[i]

    return new_str


if __name__ == '__main__':
    main()
