# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        left, right = 1, nums[0]
        step = 1
        while right < length - 1:
            for i in range(left, right + 1):  # 遍历当前能到达的所有点，取出下一次能到达的最远位置的点，并用left和right记录该点下一次能到达的区间
                if nums[i] + i > right:
                    right = nums[i] + i
                    left = i + 1
            step += 1

        return step

# nums = [2,3,1,1,4]
nums = [1,2]
# nums = [0]
solution = Solution()
print(solution.jump(nums))