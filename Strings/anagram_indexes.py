# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from collections import Counter

def main():
    s = 'cbaebabacd'
    p = 'abc'

    print(findAnagrams(s, p))


def findAnagrams(s, p):
    if len(s) < len(p):
        return []

    if len(s) == len(p):
        if s == p:
            return [0]
        return []

    good_indicies = []

    p_tracker = Counter(p)
    s_tracker = Counter(s[:len(p) - 1])

    for i in range(len(p) - 1, len(s)):
        pass



if __name__ == '__main__':
    main()
