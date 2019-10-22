# 딕셔너리 선언
딕셔너리 = {
    "문자열": "값",
    273: [1, 2, 3, 4],
    True: False
}

# 반복문
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))
# 요소 추가
딕셔너리["키"] = "값"
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))
print()
del 딕셔너리["키"]
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))

# 인덱스 출력의 세가지 방법
array = [273, 52, 103, 32, 57]

# 첫번째 i를 인덱스로 사용 - C언어 형태
i = 0
for element in array:
    print("{} : {}".format(i, element)) 
    i += 1

# 두번째 enumerate 함수 사용 - 인덱스와 값을 리턴
for i, element in enumerate(array):
    print("{} : {}".format(i, element)) 

# 세번째 range 함수 사용 - 인덱스를 이용
for i in range(len(array)):
    print("{} : {}".format(i, array[i])) 
