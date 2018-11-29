class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return False

        start = end = 0

        # for i in range(0, len(s)):





    def is_palindrome(string):
        if string == string[::-1]:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    string = 'Helloracecargoodbye'
    sol.longestPalindrome(string)