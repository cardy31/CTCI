
def main():
    str1 = 'cca'
    str2 = 'abc'

    print(detect_anagram(str1, str2))


def detect_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    table = {}

    for i in range(0, len(str1)):
        if str1[i] in table.keys():
            table[str1[i]] += 1
        else:
            table[str1[i]] = 1

    for i in range(0, len(str2)):
        if str2[i] in table.keys() and table[str2[i]] > 0:
            table[str2[i]] -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    main()
