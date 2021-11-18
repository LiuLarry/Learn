# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

# 请你实现 Trie 类：

# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Trie:
    
    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        tmp = self.dic
        for w in word:
            if w not in tmp:
                tmp[w] = {}
            tmp = tmp[w]
        tmp['is_word'] = True
        print(self.dic)

    def search(self, word: str) -> bool:
        pass


    def startsWith(self, prefix: str) -> bool:
        pass

obj = Trie()
obj.insert("apple")
obj.insert("apbc")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)