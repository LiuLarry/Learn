# 给你一个大小为 m * n 的矩阵 mat，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

# 请你返回矩阵中战斗力最弱的 k 行的索引，按从最弱到最强排序。

# 如果第 i 行的军人数量少于第 j 行，或者两行军人数量相同但 i 小于 j，那么我们认为第 i 行的战斗力比第 j 行弱。

# 军人 总是 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
from collections import Counter


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_count = [0] * len(mat) 
        for index, m in enumerate(mat):
            mat_count[index] = (index, sum(m))
            
        mat_count.sort(key=lambda x: x[1])
        print(mat_count)
            
        res = [1] * k
        for i in range(k):
            res[i] = mat_count[i][0]
            
        return res
            
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

s = Solution()
print(s.kWeakestRows(mat, 3))