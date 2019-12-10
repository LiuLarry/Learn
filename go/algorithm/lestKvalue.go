/**
题目描述

输入ｎ个整数，输出其中最小的ｋ个

输入说明
１　输入两个整数
２　输入一个整数数组

输出描述
输出一个整数数组


https://www.nowcoder.com/practice/69ef2267aafd4d52b250a272fd27052c?tpId=37&tqId=21281&tPage=3&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
*/
package main

import (
	"fmt"
	"sort"
)

func main() {
	for {
		var N, k int
		n, err := fmt.Scan(&N, &k)
		if n == 0 || err != nil {
			break
		}

		var arry []int = make([]int, N)
		for i := 0; i < N; i++ {
			//var v int
			n, err = fmt.Scan(&arry[i])
			if n == 0 || err != nil {
				return
			}
		}
		GetMinK(k, arry)
	}
	//fmt.Printf("%+v", arry)
}

// GetMinK 获取最小的Ｋ个值
func GetMinK(k int, arry []int) {
	sort.Ints(arry)
	delim := ""
	for i := 0; i < k; i++ {
		fmt.Printf("%s%d", delim, arry[i])
		delim = " "
	}
	fmt.Println()
}
