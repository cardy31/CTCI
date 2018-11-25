def reverse_words(string):
    words = string.split(' ')

    i = 0
    j = len(words) - 1
    while i < j:
        temp = words[i]
        words[i] = words[j]
        words[j] = temp
        i += 1
        j -= 1

    return ' '.join(words)


def reverse_words_no_python(string):
    index = 0
    words = ['']
    for i in range(0, len(string)):
        if string[i] != ' ':
            words[index] += string[i]
        else:
            words.append('')
            index += 1

    i = 0
    j = len(words) - 1
    while i < j:
        temp = words[i]
        words[i] = words[j]
        words[j] = temp
        i += 1
        j -= 1

    final = ''
    for word in words:
        final += word + ' '

    return final[:-1]


def reverse_words_in_place(string):
    words = string.split(' ')
    for i in range(0, len(words)):
        words[i] = reverse_string_python(words[i])

    return ' '.join(words)


def reverse_words_in_place_python(string):
    return string[-1::-1]


def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)

    temp = ''
    for i in range(0, len(stack)):
        temp += stack.pop()

    return temp


def reverse_string_python(string):
    return string[::-1]


if __name__ == '__main__':
    # print(reverse_words('one two three'))
    print(reverse_words_no_python('one two three'))
    # print(reverse_words_in_place('one two three'))
    # print(reverse_string('one two three'))
    # print(reverse_string_python('one two three'))
