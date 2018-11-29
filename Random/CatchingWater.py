# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        total = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1

        return total

    # This solution takes the problem in slices
    # Runtime is n to find max + highest peak * n
    def first_trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0:
            return 0

        highest_peak = max(height)
        hard_count = 0

        for i in range(0, highest_peak):

            start_found = False
            possible_count = 0

            for j in range(0, len(height)):
                if height[j] == 0:
                    if start_found:
                        possible_count += 1

                elif height[j] > 0:
                    height[j] -= 1

                    # We found an end so the count in between has been trapped
                    if start_found:
                        hard_count += possible_count
                        possible_count = 0
                    else:
                        start_found = True

                else:
                    print('Invalid height')
                    return 0
        return hard_count


if __name__ == '__main__':
    sol = Solution()
    input_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = sol.trap(input_arr)
    print(result)
