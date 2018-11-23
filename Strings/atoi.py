def atoi(string):
    # Strip leading/trailing space
    string = string.strip()

    if len(string) == 0:
        return 0

    # Handle minus and plus signs
    negative = False
    if string[0] == '-':
        negative = True
        string = string[1:]
    elif string[0] == '+':
        string = string[1:]

    for i in range(0, len(string)):
        if (47 < ord(string[i]) < 58) is False:
            if i == 0:
                return 0
            string = string[:i]
            break

    max_int = 2 ** 31 - 1
    # Variable for final int
    final = 0
    # Track position in the number
    multiplier = 1
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        if ord(char) < 48 or ord(char) > 57:
            break
        final += ((ord(char) - 48) * multiplier)
        multiplier *= 10
        if final > max_int:
            if negative:
                return -1 * (2 ** 31)
            return max_int

    if negative:
        final *= -1

    return final


if __name__ == '__main__':
    var = '4193 with words'
    print(atoi(var))
