package main

import (
	"fmt"
)

// Node 节点数据结构
type Node struct {
	value int
	next  *Node
}

var head *Node

func init() {
	p := &Node{
		value: 1,
		next:  nil,
	}
	head = p
	for i := 2; i < 10; i++ {
		q := &Node{
			value: i,
			next:  nil,
		}
		p.next = q
		p = p.next
	}
}

func main() {
	for p := head; p != nil; p = p.next {
		fmt.Printf("%d ", p.value)
	}

	fmt.Println()

	r := RevertSingleLink(head)
	for p := r; p != nil; p = p.next {
		fmt.Printf("%d ", p.value)
	}
	fmt.Println()
}

//RevertSingleLink 单链表逆序输出
func RevertSingleLink(n *Node) *Node {
	cur := n
	var pre *Node = nil
	var nex *Node = cur.next
	for nex != nil {
		cur.next = pre
		pre = cur
		cur = nex
		nex = nex.next
	}
	cur.next = pre
	return cur
}
