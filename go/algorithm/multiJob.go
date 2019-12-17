/**
多道批批处理调度

最短作业优先原则
*/
package main

import (
	"fmt"
	"sort"
)

func main() {

	var N []int = []int{8, 4, 3, 1, 10}
	GetMinK(3, N)
}

func GetMinK(p int, N []int) {
	sort.Ints(N)
	proc := make([]int, p)
	for i := 0; i < len(N); i++ {
		proc[0] += N[i]
		sort.Ints(proc)
	}
	sort.Ints(proc)
	fmt.Println(proc[p-1])
}

