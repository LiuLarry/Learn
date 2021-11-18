# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。

# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。

# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt1, cnt2 = 0, 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                cnt1 += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                cnt2 += 1
        if (cnt1 + cnt2) % 2 != 0:
            return -1
        n1, m1 = divmod(cnt1, 2)
        n2, m2 = divmod(cnt2, 2)
        return n1 + n2 + 2 * m1
    
# s1 = "xxyyxyxyxx"
# s2 = "xyyxyxxxyx"

s1 = "xx"
s2 = "yy"
solution = Solution()
print(solution.minimumSwap(s1, s2))