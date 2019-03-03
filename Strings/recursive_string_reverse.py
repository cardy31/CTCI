def reverse_words(string):
    stack = []
    word = ''
    for char in string:
        if char != ' ':
            word += char
        else:
            stack.append(word)
            word = ''
    stack.append(word)

    final = ''
    while stack:
        final += stack.pop()
        final += ' '

    return final[:-1]


if __name__ == '__main__':
    print(reverse_words('cheese steak jimmies'))
