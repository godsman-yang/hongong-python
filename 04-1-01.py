# 157쪽의 1번 문제의 답 쓰고 인증샷
# list_a = [0, 1, 2, 3, 4, 5, 6, 7]입니다. 다음 표의 함수들을 실행했을 때 list_a의 결과가 어떻게 나오는지 적어 보세요.

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a)
print("list_a.extend(list_a)", list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.append(10)
print("list_a.append(10)", list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.insert(3, 0)
print("list_a.insert(3, 0)", list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.remove(3)
print("list_a.remove(3)", list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.pop(3)
print("list_a.pop(3)", list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.clear()
print("list_a.clear()", list_a)
