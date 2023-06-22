# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

import sys

n=list(sys.stdin.readline().rstrip())
n.sort(reverse=True)

print("".join(n))