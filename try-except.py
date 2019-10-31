try:
  # 예외가 발생할 수 있는 가능성이 있는 코드
  number = int(input("> 정수를 입력해 주세요: "))
  print("입력 값은 {}입니다.".format(number))
except ValueError as exception:
  print("값에 문제가 있습니다.")
except IndexError as exception:
  print("인덱스트에 문제가 있습니다.")
except Exception as exception:
  # 예외가 발생했을 때 실행할 코드
  print("알수 없는 예외가 발생했습니다.")
  print(type(exception))
finally:
  # 무조건적으로 실행하는 코드
  print("무조건적으로 실행됩니다.")
