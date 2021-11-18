# https://zhuanlan.zhihu.com/p/61564531

from os import stat
from typing import List


# 最大连续1的个数 III
def longest_ones(A: List[int], K: int) -> int:
    L, R = 0, -1
    
    optim = 0

    while R < len(A):
        while R < len(A):
            R += 1
            if R == len(A):
                break
            if A[R] == 0:
                K -= 1
            if K < 0:
                break
            else:
                optim = max(optim, R - L + 1)
            
        if R == len(A):
            break
        
        while L < R:
            if A[L] == 0:
                K += 1
            L += 1
            
            if K > 0:
                break
        
    return optim
        
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(longest_ones(nums, 3)) 


# 无重复字符的最长子串
def length_of_longest_substring(s: str) -> int:
    L, R = 0, -1
    optim = 0
    
    status = set()
    while R < len(s):
        while R < len(s):
            R += 1
            if R == len(s):
                break
            if s[R] not in status:
                status.add(s[R])
                optim = max(optim, R - L + 1)
            else:
                break
            
        if R == len(s):
            break
        
        while L < R:
            if s[L] != s[R]:
                status.remove(s[L])
                L += 1
            else:
                L += 1
                break            
    return optim
    
print(length_of_longest_substring("abcabcbb"))


# 暴力解法
def solver(nums, s):
    optim = len(nums) + 1
    for start in range(len(nums)):
        summation = 0
        for end in range(start, len(nums)):
            summation += nums[end]
            if summation >= s:
                optim = min(optim, end - start + 1) 
                break
    return optim

nums = [2,3,1,2,4,3]
optim = solver(nums, 7)
print(optim)


# 长度最小的子数组
def min_sub_array_len(s: int, nums: List[int]) -> int:
    summation = 0
    L, R = 0, -1
    optim = len(nums) + 1
    while R < len(nums):
        while R < len(nums):
            R += 1
            if R < len(nums):
                summation += nums[R]
            if summation >= s:
                optim = min(optim, R - L + 1)
                break

        if R == len(nums):
            break

        while L < R:
            summation -= nums[L]
            L += 1
            if summation >= s:
                optim = min(optim, R - L + 1)
            else:
                break
    return optim if optim != len(nums) + 1 else 0

optim = min_sub_array_len(7, nums)
print(optim)
