# 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def power(x, y):
    return x ** y



# __name__ 사용
# 실행하는 위치가 다르면 실행 안됨
print(__name__)
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__!')
    print(add(5, 5))
    print(sub(15, 5))
    print(mul(5, 5))
    print(div(10, 2))
    print(power(5, 3))
    print('-' * 15)
