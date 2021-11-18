# defaultdict数据结构
from collections import defaultdict

dict1 = defaultdict(list)
dict2 = defaultdict(int)

dict1['a'] = [1]
dict1['a'].append(2)
dict2['a'] = 1
print(dict1, dict2)
print(dict1['a'], dict2['a'])

# deque
from collections import deque

d = deque()
d.appendleft(1)
d.appendleft(2)
d.append(3)
d.append(4)
d.append(5)
print(d)
print(d.popleft(), d)
print(d.pop(), d)

for i in d:
    print(i, end=",")