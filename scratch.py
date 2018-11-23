def main():
    print(lengthOfLongestSubstring('aab'))


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    table = {}

    curr_max = running_max = 0

    oldest_index = 0

    for i in range(0, len(s)):
        oldest_index = i - running_max
        # We've seen this char before
        if s[i] in table.keys():

            # If the char was last seen in our current frame...
            if table[s[i]][-1] >= oldest_index:
                curr_max = max(curr_max, running_max)
                running_max = i - table[s[i]][-1]
                table[s[i]].append(i)

            else:
                table[s[i]].append(i)
                running_max += 1
        # Char is new to us
        else:
            # Add to the table, increment the running max
            table[s[i]] = [i]
            running_max += 1
    return max(curr_max, running_max)


if __name__ == '__main__':
    main()
