def print_n_times(value, n):
    for i in range(n):
        print(value)

def function(일반매개변수A, 일반매개변수B, *가변매개변수, 기본매개변수A=10, 기본매개변수B=20):
    print(일반매개변수A, 일반매개변수B)
    print(가변매개변수)
    print(기본매개변수A, 기본매개변수B)
    
def function2(일반매개변수A, 일반매개변수B, 기본매개변수A=10, 기본매개변수B=20):
    print(일반매개변수A, 일반매개변수B)
    print(기본매개변수A, 기본매개변수B)

print()
print_n_times("안녕하세요", 1)
print_n_times("안녕하세요", 5)

function(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
function2(0, 1, 2, 3)
