import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# 0과 가장 가까운 값 찾기

n = int(input()) # 분석할 온도의 개수를 읽어와 n에 저장한다


if n == 0:  # 온도가 없을 경우에는 0을 출력하기
    print("0")
else:
    min_t = 5527  # 절대값 비교하기 위해 가장 큰 값을 초깃값으로 설정하고 비교
    for i in input().split(): 
        # t: a temperature expressed as an integer ranging from -273 to 5526
        # t는 온도를 의미하며 -273에서 5526의 벙위를 가진다
        t = int(i)
        if abs(t) < abs(min_t):  # 절대값이 t가 작으면 t를 가장 작은값으로 넣기
            min_t = t
        elif abs(t) == abs(min_t): # 절대값이 서로 같을때는  양수로 처리하기
            if t>0:  # t가 0보다 크면 (양수이면)
                min_t =t # t를 가장작은값에서 양수를 적용하기
    print(min_t)
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)