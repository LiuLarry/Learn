#!/bin/bash
# 使用函数的输出作为返回值

function fun_output {
    read -p "Enter a value: " value
    echo $[ $value * 2 ]
}

result=`fun_output`
echo $result
