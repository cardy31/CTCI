def main():
    str1 = "aabcccccaaa"
    print(string_compress(str1))


# Runtime: O(n)
def string_compress(str1):
    letter = str1[0]
    count = 0
    final = ''

    for character in str1:
        if letter == character:
            count += 1
        else:
            final += letter
            final += count.__str__()
            letter = character
            count = 1

    final += letter
    final += count.__str__()

    if len(final) < len(str1):
        return final
    return str1


if __name__ == '__main__':
    main()
