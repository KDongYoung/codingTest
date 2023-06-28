'''
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''
import sys
from collections import Counter

n=int(sys.stdin.readline())

nums=[]

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()  

# 최빈값 -> 딕셔너리로 접근 OR Ccounter
count=Counter(nums).most_common(2) #[(key,value), (key,value)]

# arr=dict({})
# for num in nums:
#     if num in arr:
#         arr[num]+=1
#     else:
#         arr[num]=1

# mx=max(arr.values())
# a=[key for key in arr if arr[key]==mx]

# if len(a)>1:
#     print(a[1])
# else:
#     print(a[0])

    
print(round(sum(nums)/n)) # 산술평균
print(nums[n//2]) # 중앙값

if len(count)>1 and count[0][1]==count[1][1]: # 빈도수가 같은 것이 여러 개인 경우
    print(count[1][0])
else:
    print(count[0][0])
    
print(nums[-1]-nums[0]) # 범위
