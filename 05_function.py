# Function
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수의 정의 방법
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print("Hello, ", w)


word = "Goodboy"

first_func(word)


# 예제2
def return_func(w1):
    return "Hello, " + str(w1)


print(return_func("Goodboy2"))


# 예제3 (다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


y1, y2, y3 = func_mul(10)

print(y1, y2, y3)


# 예제3 (튜플리턴)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(10)
print(type(q), q, list(q))


# 예제3 (리스트리턴)
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(10)
print(type(p), p, set(p))


# 예제4 (딕셔너리 리턴)
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return dict(
        v1=y1,
        v2=y2,
        v3=y3
    )


r = func_mul3(10)
print(type(r), r, r.items(), r.get('v2'))


# 중요
# *args, **kwargs

# *args (언팩킹) : 가변 매개변수
def args_func(*args):   # 매개변수 명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-------')


args_func('Lee')
args_func('Lee', 'Pard')


# kwargs (언팩킹)
def kwargs_func(**kwargs):  # 매개변수 명은 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')


kwargs_func(name='test', test='name')


# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)


# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)


nested_func(100)
# func_in_func(100) 실행 불가


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 시행 함수(Heep 초기화) -> 메모리 초기화
# 남발 시 가독성이 오히려 감소
# def mul_func(x, y):
#    return x * y
# 위 함수와 동일
# a= lambda x, y: x * y
def mul_func(x, y):
    return x * y

q = mul_func(10, 50)
print(q)
mul_func_var = mul_func
print(mul_func_var(20, 50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50, 50))


def func_final(x, y, func):
    print(x * y * func(100, 100))


func_final(10, 20, lambda x,y: x*y)