# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

# 你需要计算完成所有任务所需要的 最短时间 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/task-scheduler
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        
        max_tasks = freq[max(freq, key=lambda x: freq[x])]
        
        res = (max_tasks - 1 ) * (n+1)
        
        for i in freq:
            if freq[i] == max_tasks:
                res += 1
                
        if res < len(tasks):
            res = len(tasks)
            
        return res
        
tasks = ["A","A","A","B","B","B"]
s = Solution()
print(s.leastInterval(tasks, 2))