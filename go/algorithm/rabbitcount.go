/**
统计每个月的兔子总数

有一只兔子，从出生后第三个月起每个月生一只兔子，小兔子长到第三个月
后每个月又生一只兔子，假如兔子不会死，则每个月兔子的总数是多少？
*/
package main

import "fmt"

func main() {
	for {
		var mouth int
		n, err := fmt.Scan(&mouth)
		if n == 0 || err != nil {
			break
		}
		count := getTotalCount(mouth)
		fmt.Println(count)
	}
}

func getTotalCount(mouth int) int {
	a1, a2, a3 := 1, 0, 0
	for n := 2; n <= mouth; n++ {
		tmp := a1
		a1 = a2 + a3
		a3 = a3 + a2
		a2 = tmp
	}
	return a1 + a2 + a3
}
