class Solution:
    # This one is messy and most likely not an interview question
    def longestPalindrome(self, s):
        if len(s) > 1000:
            return 'Invalid Input String'

        curr_start = 0
        curr_end = 0
        max_index = len(s) - 1
        for i in range(0, len(s)):
            if curr_end - curr_start == 0:
                curr_end = i
                continue
            pal_len = (curr_end - curr_start) + 1

            separator = 0
            if pal_len % 2 == 0:
                separator = pal_len // 2
            else:
                separator = (pal_len // 2) + 1

            is_pal = True
            for i in range(curr_start, curr_end - (pal_len // 2)):
                if s[i] != s[i + separator]:
                    is_pal = False
                    break









if __name__ == '__main__':
    solution = Solution()
    s = 'racecar'
    print(solution.longestPalindrome(s))
