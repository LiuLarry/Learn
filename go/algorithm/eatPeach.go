/**
猴子吃桃

孙悟空喜欢吃蟠桃。。。
以知蟠桃园里有N棵蟠桃树，第i棵蟠桃树上有N[i](大于0)个蟠桃，天兵
天将将在H(不小于蟠桃树棵树)小时后回来。孙悟空可以决定他吃蟠桃的
速度K(单位：个/小时)，每小时他会选择一棵蟠桃树，从中吃掉K个蟠桃，
如果这棵树上的蟠桃小于K，他将吃掉树上所有的蟠桃，然后一个小时内不
再吃其余蟠桃树上的蟠桃。孙悟空喜欢慢慢吃，但仍想再天兵天将回来前吃
掉所有的，求孙悟空可以在H小时内吃掉所有蟠桃的最小速度K(K为整数)
*/
package main

import "fmt"

func main() {

	var N []int = []int{3, 5, 2, 10, 14, 40, 15}
	GetMinK(10, N)
}

func GetMinK(hour int, N []int) {
	l := len(N)
	sum := 0
	max := 0
	for i := 0; i < l; i++ {
		sum += N[i]
		if max < N[i] {
			max = N[i]
		}
	}

	for K := sum/l + 1; K < max; K++ {
		v := 0
		for i := 0; i < l; i++ {
			v += N[i] / K
			if N[i]%K != 0 {
				v++
			}
		}
		if v <= hour {
			fmt.Println(K)
			break
		}
	}
}
