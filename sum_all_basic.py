# 함수를 선언합니다.
def sum_all(start, end):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end):
        output += i
    return output

start = 1
end = 1001
print("sum_all({}, {}) 결과: {}".format(start, end, sum_all(start, end)))