# https://leetcode-cn.com/problems/short-encoding-of-words/

# 单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：

# words.length == indices.length
# 助记字符串 s 以 '#' 字符结尾
# 对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等
# 给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。

#  

# 作者：nettee
# 链接：https://leetcode-cn.com/problems/short-encoding-of-words/solution/wu-xu-zi-dian-shu-qing-qing-yi-fan-zhuan-jie-guo-j/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List


def minimumLengthEncoding(words: List[str]) -> int:
    N = len(words)
    # 逆序字典序排序    
    words.sort(key=lambda word: word[::-1])

    res = 0
    for i in range(N):
        if i+1 < N and words[i+1].endswith(words[i]):
            # 当前单词是下一个单词的后缀，丢弃
            pass
        else:
            res += len(words[i]) + 1 # 单词加上一个 '#' 的长度
    
    return res

words = ["time", "me", "bell"]

print(minimumLengthEncoding(words))