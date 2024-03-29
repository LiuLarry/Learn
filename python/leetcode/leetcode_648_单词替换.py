# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

# 现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

# 你需要输出替换之后的句子。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/replace-words
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        words = sentence.split(" ")
        
        res = []
        
        for word in words:
            found = False
            for d in dictionary:
                if word.startswith(d):
                    res.append(d)
                    found = True
                    break
            if not found:
                res.append(word)
    
        return " ".join(res)

# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"

solution = Solution()
replace = solution.replaceWords(dictionary, sentence)
print(replace)