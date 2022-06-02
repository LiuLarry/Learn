# https://zhuanlan.zhihu.com/p/26465701

def next_exceed(input: list):
    result = [-1 for _ in input]
    stack = []
    
    for index, val in enumerate(input):
        while len(stack) > 0 and input[stack[-1]] < val:
            result[stack[-1]] = index - stack[-1]
            stack.pop()
        stack.append(index)

    print(result)


input = [5,3,1,2,4]
next_exceed(input)